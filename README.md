# Tasks Flask CRUD

API REST simples para gerenciamento de tarefas (tasks), desenvolvida em Python com Flask, implementando as quatro operações fundamentais de um CRUD: **Create, Read, Update e Delete**.

## 🚀 Tecnologias

- Python
- Flask
- Pytest e Requests (testes automatizados)

## 📌 Sobre o projeto

A API permite criar, listar, buscar, atualizar e deletar tarefas. Cada tarefa é representada pela classe `Task` e possui os seguintes atributos:

- `id`: identificador único, gerado automaticamente
- `title`: título da tarefa
- `description`: descrição da tarefa
- `completed`: status de conclusão (booleano, `false` por padrão)

> **Nota:** os dados são armazenados em memória (em uma lista Python), e não em um banco de dados. Isso significa que as tarefas são perdidas ao reiniciar a aplicação — uma escolha proposital para focar no aprendizado da lógica de rotas, requisições HTTP e testes de API com Flask.

## 📂 Estrutura do projeto

\`\`\`
tasks-flask-crud/
├── models/
│   └── task.py         # Classe Task
├── app.py               # Rotas da API (CRUD)
├── tests.py              # Testes automatizados de integração
└── requirements.txt
\`\`\`

## 🔗 Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/tasks` | Cria uma nova tarefa |
| GET | `/tasks` | Lista todas as tarefas e o total |
| GET | `/tasks/<id>` | Busca uma tarefa específica pelo ID |
| PUT | `/tasks/<id>` | Atualiza uma tarefa existente |
| DELETE | `/tasks/<id>` | Remove uma tarefa |

## ▶️ Como executar o projeto

1. Clone o repositório
\`\`\`bash
git clone https://github.com/thispedroo/tasks-flask-crud
cd tasks-flask-crud
\`\`\`

2. Instale as dependências
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. Execute a aplicação
\`\`\`bash
python app.py
\`\`\`

A API ficará disponível em `http://127.0.0.1:5000`.

## 📋 Exemplos de uso

**Criar uma tarefa**
\`\`\`bash
curl -X POST http://127.0.0.1:5000/tasks \\
  -H "Content-Type: application/json" \\
  -d '{"title": "Estudar Flask", "description": "Revisar rotas e métodos HTTP"}'
\`\`\`

**Listar todas as tarefas**
\`\`\`bash
curl http://127.0.0.1:5000/tasks
\`\`\`

**Buscar uma tarefa específica**
\`\`\`bash
curl http://127.0.0.1:5000/tasks/1
\`\`\`

**Atualizar uma tarefa**
\`\`\`bash
curl -X PUT http://127.0.0.1:5000/tasks/1 \\
  -H "Content-Type: application/json" \\
  -d '{"title": "Estudar Flask", "description": "Revisado", "completed": true}'
\`\`\`

**Deletar uma tarefa**
\`\`\`bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
\`\`\`

## ✅ Testes

Os testes automatizados (`tests.py`) validam o fluxo completo do CRUD (criação, listagem, busca, atualização e deleção) fazendo requisições HTTP reais para a API.

Como eles dependem do servidor rodando, é preciso:

1. Deixar a aplicação rodando em um terminal:
\`\`\`bash
python app.py
\`\`\`

2. Em outro terminal, rodar os testes com pytest:
\`\`\`bash
pytest tests.py
\`\`\`

## 📝 Autor

Desenvolvido por [João Pedro](https://github.com/thispedroo).