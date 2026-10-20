"""
Pipeline de Ingestão de Dados de Clientes para o Webhook do n8n.
Simula a extração de uma base de dados interna/CRM e realiza o disparo
seguro via requisição HTTP POST autenticada por Header.
"""

import json
import requests

# URL pública ou webhook de teste gerado pelo n8n
WEBHOOK_URL = "https://seu-endpoint.n8n.cloud/webhook/investments-briefing"
API_AUTH_TOKEN = "dio_rpa_secure_token_2026"

# Payload estruturado com dados do investidor e composição de carteira
dados_investidor = {
    "id_cliente": "CLI-88492",
    "nome": "Investidor Exemplo",
    "email": "investidor@exemplo.com",
    "perfil": "Moderado / Crescimento",
    "carteira": [
        {"ticker": "PETR4", "peso": "30%"},
        {"ticker": "VALE3", "peso": "40%"},
        {"ticker": "ITUB4", "peso": "30%"}
    ]
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_AUTH_TOKEN
}

def disparar_extracao():
    print("[*] Iniciando disparo do pipeline para o n8n...")
    try:
        response = requests.post(
            WEBHOOK_URL,
            data=json.dumps(dados_investidor),
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            print("[+] Payload recebido e fluxo acionado com sucesso no n8n.")
        else:
            print(f"[-] Erro na chamada: HTTP {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as err:
        print(f"[!] Falha na conexão com o endpoint: {err}")

if __name__ == "__main__":
    disparar_extracao()
