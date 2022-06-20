from flask import jsonify
from Model.Task import Task
from data.Tasks import tasks
import datetime

class TaskController:
    def __init__(self) -> None:
        pass

    def getTasks(self):
        return jsonify({'tasks': tasks})

    def getTask(self, id):
        taskFound = [
            task for task in tasks if task['id'] == id.lower()]
        if (len(taskFound) > 0):
            #return jsonify({'task': taskFound[0]})
            return taskFound[0]
        return False

    def addTask(self, task):
        response = False
        new_task = {
            'id': task.id,
            'title': task.title,
            'done': task.done,
            'created_at': task.created_at,
            'updated_at': task.updated_at
        }
        # TODO: validar que el "id" no exista
        tasks.append(new_task)
        response = True
        return response

    def updateTask(self, task, task_editted):
        response = False
        task['id'] = task_editted.id
        task['title'] = task_editted.title
        task['done'] = task_editted.done
        task['updated_at'] = task_editted.updated_at
        response = True
        return response