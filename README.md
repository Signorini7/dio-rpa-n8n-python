# Assistente de Análise de Investimentos com RPA (n8n + Python)

Pipeline de automação de ponta a ponta (RPA) desenvolvido durante a formação na DIO, integrando scripts em Python, orquestração de fluxos no n8n e distribuição automatizada por e-mail.

---

## 🛠️ Tecnologias e Ferramentas
- **Python / Google Colab:** Coleta, higienização e estruturação dos dados de mercado em JSON.
- **n8n:** Orquestração de webhooks, controlo de fluxo condicional, tratamento via nós de código e junção de dados (*Merge*).
- **LLM / Agentes de IA:** Análise contextualizada e geração automática do briefing executivo financeiro.
- **Gmail:** Envio programado do relatório final diretamente para a caixa de correio do destinatário.

---

## 🏗️ Arquitetura do Processo
1. **Extração de Dados:** Script Python envia as informações de mercado via pedido HTTP POST para o endpoint do n8n.
2. **Segurança:** O webhook do n8n encontra-se protegido por autenticação via cabeçalho (`Header Auth`), rejeitando pedidos não autorizados.
3. **Cruzamento e Formatação:** O fluxo unifica os dados complementares via nós de *Merge* e prepara o prompt estruturado com nós de *Code*.
4. **Inteligência Artificial:** A API de LLM processa o conteúdo consolidado e gera a recomendação resumida.
5. **Distribuição:** O nó do Gmail realiza o envio automático do relatório formatado.
