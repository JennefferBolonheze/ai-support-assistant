from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    message = data.get("message", "").lower().strip()

    if not message:
        return jsonify({
            "error": "Nenhuma solicitação foi informada."
        }), 400


    # =========================
    # PALAVRAS-CHAVE
    # =========================

    categories = {

        "Acesso": [
            "acesso",
            "login",
            "senha",
            "entrar",
            "bloqueado",
            "conta",
            "usuário"
        ],

        "Rede": [
            "internet",
            "wifi",
            "wi-fi",
            "rede",
            "conexão",
            "conectar",
            "vpn"
        ],

        "Hardware": [
            "computador",
            "notebook",
            "monitor",
            "teclado",
            "mouse",
            "impressora",
            "equipamento"
        ],

        "Software": [
            "sistema",
            "programa",
            "aplicativo",
            "app",
            "erro",
            "travando",
            "instalar",
            "atualizar"
        ],

        "E-mail": [
            "email",
            "e-mail",
            "outlook",
            "mensagem",
            "caixa de entrada"
        ],

        "Dados": [
            "dados",
            "relatório",
            "planilha",
            "excel",
            "power bi",
            "dashboard",
            "banco de dados"
        ]

    }


    # =========================
    # PRIORIDADE
    # =========================

    high_priority_words = [
        "urgente",
        "agora",
        "imediatamente",
        "parado",
        "bloqueado",
        "não consigo trabalhar",
        "produção",
        "reunião",
        "cliente",
        "prazo hoje"
    ]

    medium_priority_words = [
        "hoje",
        "preciso",
        "problema",
        "erro",
        "falha",
        "não funciona"
    ]


    # =========================
    # IDENTIFICA CATEGORIA
    # =========================

    detected_category = "Outros"
    detected_keywords = []

    highest_matches = 0


    for category, keywords in categories.items():

        matches = []

        for keyword in keywords:

            if keyword in message:
                matches.append(keyword)

        if len(matches) > highest_matches:

            highest_matches = len(matches)

            detected_category = category

            detected_keywords = matches


    # =========================
    # IDENTIFICA PRIORIDADE
    # =========================

    priority = "Baixa"


    if any(
        word in message
        for word in high_priority_words
    ):

        priority = "Alta"

    elif any(
        word in message
        for word in medium_priority_words
    ):

        priority = "Média"


    # =========================
    # RESPOSTA SUGERIDA
    # =========================

    responses = {

        "Acesso":
            "Olá! Identificamos que sua solicitação está relacionada a acesso. Verifique suas credenciais e, caso o problema continue, recomendamos validar o status da conta e solicitar apoio ao responsável pelo sistema.",

        "Rede":
            "Olá! Identificamos um possível problema de conectividade. Verifique sua conexão com a rede, Wi-Fi ou VPN e tente reconectar. Caso o problema continue, encaminhe as informações do erro para análise técnica.",

        "Hardware":
            "Olá! Sua solicitação parece estar relacionada a um equipamento. Recomendamos verificar cabos, energia e conexões básicas. Se o problema persistir, será necessário suporte técnico no dispositivo.",

        "Software":
            "Olá! Identificamos uma possível falha de software. Tente reiniciar a aplicação e verificar se há atualizações disponíveis. Caso o erro permaneça, envie a mensagem apresentada pelo sistema.",

        "E-mail":
            "Olá! Sua solicitação está relacionada ao serviço de e-mail. Recomendamos verificar a conexão, credenciais e sincronização da conta. Se necessário, encaminhe a mensagem de erro apresentada.",

        "Dados":
            "Olá! Identificamos uma solicitação relacionada a dados ou relatórios. Verifique a fonte dos dados, permissões de acesso e a última atualização das informações antes de prosseguir.",

        "Outros":
            "Olá! Recebemos sua solicitação. Para direcionarmos o atendimento corretamente, recomendamos fornecer mais detalhes sobre o problema, o sistema envolvido e quando a situação começou."
    }


    suggested_response = responses[
        detected_category
    ]


    return jsonify({

        "category":
            detected_category,

        "priority":
            priority,

        "keywords":
            detected_keywords,

        "response":
            suggested_response

    })


if __name__ == "__main__":
    app.run(debug=True)