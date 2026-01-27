from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar e Deletar
# Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})


@app.route('/tasks', methods=['GET'])
def get_tasks():
# Segunda e melhor forma:
    task_list = [task.to_dict() for task in tasks]

# Primeira forma:
#    for task in tasks:
#        task_list.append(task.to_dict())

    output = {
                "tasks": task_list,
                "total_tasks": 0
            }
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
