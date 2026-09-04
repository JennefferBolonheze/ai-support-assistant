# 🤖 AI Support Assistant

Assistente inteligente para análise e classificação automática de solicitações de suporte.

O projeto recebe uma descrição escrita pelo usuário, identifica palavras-chave relevantes e classifica automaticamente o chamado por **categoria** e **prioridade**, além de apresentar uma **resposta sugerida para o atendimento**.

---

## ✨ Funcionalidades

- Análise de solicitações de suporte
- Identificação automática de palavras-chave
- Classificação por categoria
- Classificação de prioridade
- Geração de respostas sugeridas
- Comunicação entre frontend e backend sem recarregar a página
- Interface responsiva em dark mode

### Categorias disponíveis

- 🔐 Acesso
- 🌐 Rede
- 🖥️ Hardware
- 💻 Software
- 📧 E-mail
- 📊 Dados
- 📁 Outros

### Níveis de prioridade

- 🔴 Alta
- 🟡 Média
- 🟢 Baixa

---

## 🧠 Como funciona?

O usuário descreve um problema, por exemplo:

> Minha internet caiu e tenho uma reunião com cliente agora.

A aplicação envia a solicitação para o backend desenvolvido em Python.

O sistema analisa o conteúdo, identifica termos relevantes e retorna informações como:

```text
Categoria: Rede
Prioridade: Alta
Palavras detectadas: internet, reunião, cliente, agora
```

Além da classificação, o sistema apresenta uma resposta sugerida de acordo com o tipo de solicitação.

---

## 🏗️ Arquitetura

```text
Usuário
   ↓
HTML + CSS
   ↓
JavaScript
   ↓
Flask API
   ↓
Python
   ↓
Análise de texto
   ↓
Categoria + Prioridade + Resposta
   ↓
Interface
```

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- JavaScript
- HTML5
- CSS3
- REST API / JSON
- Git
- GitHub

---

## 📂 Estrutura do projeto

```text
ai-support-assistant/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

> O ambiente virtual `.venv` não é versionado no repositório.

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone <URL-DO-REPOSITORIO>
```

Entre na pasta:

```bash
cd ai-support-assistant
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## 🔎 Exemplo de uso

### Solicitação

```text
Não consigo acessar o sistema e preciso enviar um relatório hoje.
```

### Resultado

A aplicação analisa o texto e apresenta a categoria identificada, o nível de prioridade, as palavras-chave encontradas e uma sugestão de resposta para o atendimento.

---

## 💡 Sobre a classificação

A versão atual utiliza uma abordagem **rule-based**, baseada em regras e palavras-chave definidas no backend.

Isso permite que as decisões do sistema sejam explicáveis e executadas localmente, sem depender de serviços externos.

O projeto pode evoluir futuramente para uma versão utilizando modelos de Inteligência Artificial para classificação contextual e geração dinâmica de respostas.

---

## 🔮 Próximas melhorias

- Integração com modelo de IA
- Classificação contextual com NLP
- Geração dinâmica de respostas
- Histórico de solicitações
- Dashboard com métricas dos chamados
- Persistência de dados em banco de dados
- Autenticação de usuários

---

## 👩‍💻 Autora

**Jenneffer Souza Bolonheze**

Estudante de Sistemas de Informação, com interesse em Inteligência Artificial, automação, dados e desenvolvimento de soluções tecnológicas.