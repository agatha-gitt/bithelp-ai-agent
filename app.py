# -*- coding: utf-8 -*-

import gradio as gr
import requests
import json

# Variável global para manter o histórico na memória da sessão
historico_memoria = []

# 2. LÓGICA DO AGENTE (Atualizada com Histórico)
def ai_agente(prompt, perfil):
    global historico_memoria

    if not prompt.strip():
        return "⚠️ Por favor, digite sua dúvida técnica!", "\n".join(historico_memoria)

    # 1. Definimos a Persona
    contextos_disponiveis = {
        "Analista de Suporte N1": "Você é um Analista especialista de Suporte Técnico N1.",
        "Engenheiro de Segurança (Cibersegurança)": "Você é um Engenheiro especialista em Segurança Digital e Cibersegurança.",
        "Administrador de Redes e Infraestrutura": "Você é um Administrador especialista em Redes e Infraestrutura de TI."
    }

    # 2. Definimos a Regra de Formato
    instrucao_obrigatoria = (
        "\nSua resposta DEVE ser estruturada obrigatoriamente assim:\n"
        "1. [DIAGNÓSTICO]: Classifique como Login, Instalação ou Configuração.\n"
        "2. [SEVERIDADE]: 🔴 Alta, 🟡 Média ou 🟢 Baixa.\n"
        "3. [SOLUÇÃO]: Procedimento passo a passo técnico.\n"
        "Se a severidade for Alta, encerre com: 'Um técnico humano foi notificado'."
    )

    persona = contextos_disponiveis.get(perfil, "Você é um especialista em TI.")

    # Incluímos o histórico recente no contexto para a IA ter "memória"
    memoria_contexto = "\n".join(historico_memoria[-50:]) # Pega as últimas 50 interações
    contexto_final = f"{persona} {instrucao_obrigatoria}\n\nHistórico recente:\n{memoria_contexto}"

    body = {
        "contents": [
            {
                "parts": [{"text": f"{contexto_final}\n\nPergunta atual:\n {prompt} "}]
            }
        ]
    }

    try:
        response = requests.post(
            URL, # Certifique-se que a variável URL está definida com sua chave
            headers={"Content-Type": "application/json"},
            data=json.dumps(body),
            timeout=30
        )
        if response.status_code != 200:
            return f"Erro {response.status_code}:\n{response.text}", "\n".join(historico_memoria)

        data = response.json()
        resposta_ia = data["candidates"][0]["content"]["parts"][0]["text"]

        # ADICIONANDO AO HISTÓRICO
        entrada_historico = f"Usuário: {prompt}\nAgent ({perfil}): {resposta_ia}\n{'-'*40}"
        historico_memoria.append(entrada_historico)

        return resposta_ia, "\n".join(historico_memoria)

    except Exception as e:
        return f"Falha na requisição:\n{str(e)}", "\n".join(historico_memoria)

# Função para limpar o histórico
def limpar_tudo():
    global historico_memoria
    historico_memoria = []
    return "", "Analista de Suporte N1", "", "Histórico de memória vazio."

# 3. INTERFACE VISUAL
with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("# 🤖 AI Agente Inteligente de Suporte TI - BitHelp")
    gr.Markdown("Agent com interface web e histórico de memória ativa.")

    with gr.Row():
        with gr.Column(scale=1):
            entrada_texto = gr.Textbox(
                label="Digite sua solicitação",
                placeholder="Como posso ajudar?",
                lines=8
            )

            perfil_dropdown = gr.Dropdown(
                label="Perfil do Agent",
                choices=[
                    "Analista de Suporte N1",
                    "Engenheiro de Segurança (Cibersegurança)",
                    "Administrador de Redes e Infraestrutura"
                ],
                value="Analista de Suporte N1"
            )

            with gr.Row():
                btn_limpar = gr.Button("Limpar Conversa")
                btn_enviar = gr.Button("Enviar para o BitHelp", variant="primary")

        with gr.Column(scale=1):
            saida_texto = gr.Textbox(
                label="Resposta Atual do BitHelp",
                lines=10,
                interactive=False
            )

            # NOVO: Campo de Histórico de Memória
            historico_visual = gr.Textbox(
                label="📜 Histórico de Memória (Pesquisas Anteriores)",
                lines=10,
                interactive=False,
                value="Nenhuma pesquisa realizada ainda."
            )
            btn_flag = gr.Button("Flag")

    # Mapeamento de eventos atualizado para retornar 2 saídas
    btn_enviar.click(
        fn=ai_agente,
        inputs=[entrada_texto, perfil_dropdown],
        outputs=[saida_texto, historico_visual]
    )

    btn_limpar.click(
        fn=limpar_tudo,
        outputs=[entrada_texto, perfil_dropdown, saida_texto, historico_visual]
    )

demo.launch(share=True, debug=True)
