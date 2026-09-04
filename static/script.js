const supportForm =
    document.getElementById("supportForm");

const requestInput =
    document.getElementById("request");

const categoryElement =
    document.getElementById("category");

const priorityElement =
    document.getElementById("priority");

const responseElement =
    document.getElementById("response");

const keywordsElement =
    document.getElementById("keywords");


supportForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();

        const message =
            requestInput.value.trim();


        if (!message) {
            return;
        }


        categoryElement.textContent =
            "Analisando...";

        priorityElement.textContent =
            "Analisando...";

        responseElement.innerHTML =
            "<p>✨ Processando solicitação...</p>";


        try {

            const response =
                await fetch(
                    "/analyze",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify({
                                message: message
                            })
                    }
                );


            const data =
                await response.json();


            if (!response.ok) {
                throw new Error(
                    data.error ||
                    "Erro ao analisar solicitação."
                );
            }


            categoryElement.textContent =
                data.category;

            priorityElement.textContent =
                data.priority;


            responseElement.innerHTML =
                `<p>${data.response}</p>`;


            keywordsElement.innerHTML = "";


            if (
                data.keywords &&
                data.keywords.length > 0
            ) {

                data.keywords.forEach(
                    keyword => {

                        const span =
                            document.createElement(
                                "span"
                            );

                        span.className =
                            "keyword";

                        span.textContent =
                            keyword;

                        keywordsElement
                            .appendChild(span);

                    }
                );

            } else {

                keywordsElement.innerHTML =
                    `
                    <span class="keyword">
                        Nenhuma palavra-chave específica
                    </span>
                    `;

            }

        }

        catch (error) {

            categoryElement.textContent =
                "Erro";

            priorityElement.textContent =
                "Erro";

            responseElement.innerHTML =
                `<p>${error.message}</p>`;

        }

    }
);