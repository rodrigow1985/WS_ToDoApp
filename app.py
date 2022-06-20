from crypt import methods
from flask import Flask, jsonify, request
import datetime
from Controller.TaskController import TaskController
from Model.Task import Task
from data.Tasks import tasks

app = Flask(__name__)
tasks = TaskController()

# Every tasks
@app.route('/tasks', methods=['GET'])
def getTasks():
    return tasks.getTasks()

# Single Task
@app.route('/tasks/<string:task_id>', methods=['GET'])
def getTask(task_id):
    taskFound = tasks.getTask(task_id)
    if (taskFound != False):
        return jsonify({'task': taskFound})
    return jsonify({'message': 'Task Not found'})

# Create task
@app.route('/tasks', methods=['POST'])
def addTask():
    new_task = Task(request.json['id'], request.json['title'], request.json['done'], 
        datetime.datetime.now(), datetime.datetime.now())
    if (tasks.addTask(new_task)):
        return tasks.getTasks()
    return jsonify({'message': 'Task can not be added'})
    
#Update task
@app.route('/tasks/<string:task_id>', methods=['PUT'])
def editTask(task_id):
    taskFound = tasks.getTask(task_id)
    task_editted = Task(request.json['id'], request.json['title'], request.json['done'], 
        ' ', datetime.datetime.now())
    if(tasks.updateTask(taskFound, task_editted)):
        return jsonify({
            'message': 'Task Updated',
            'product': tasks.getTask(task_id)
        })
    return jsonify({'message': 'Task Not found'})

if __name__ == '__main__':
    app.run(debug=True, port=4000, host='0.0.0.0')