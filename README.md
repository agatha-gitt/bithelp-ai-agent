# 🤖 BitHelp - AI Agente Inteligente de Suporte Técnico

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

Projeto de Inteligência Artificial que simula um agente de suporte técnico com memória, múltiplos perfis e respostas estruturadas.

---

## 🚀 Sobre o Projeto

O **BitHelp** é um agente de IA desenvolvido em Python com interface web, capaz de:

- Simular atendimento técnico real
- Classificar problemas automaticamente
- Gerar soluções passo a passo
- Manter histórico de conversas (memória)

---

## 🧠 Funcionalidades

✅ Memória de interações  
✅ Perfis técnicos especializados:
- Analista de Suporte N1  
- Engenheiro de Segurança (Cibersegurança)  
- Administrador de Redes  

✅ Classificação automática:
- Diagnóstico (Login, Instalação, Configuração)  
- Severidade (Alta, Média, Baixa)  

✅ Interface web interativa com Gradio  

---

## 🖥️ Demonstração

Interface do sistema:

![Demo](assets/demo.png)

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Gradio
- Requests
- API de Inteligência Artificial

---

## 🏗️ Arquitetura do Sistema

O BitHelp é estruturado em três componentes principais:

- **Interface (Gradio):** interação com o usuário  
- **Lógica do agente:** processamento do prompt e definição de persona  
- **Memória:** armazenamento do histórico de interações na sessão  

---

## 📦 Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/agatha-gitt/bithelp-ai-agent.git
cd bithelp-ai-agent
