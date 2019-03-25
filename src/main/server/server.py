from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

TODOS = {
    'task1': {'task': 'build an API', 'taskDescription': 'bla', 'status': 'false'},
    'task2': {'task': 'build an', 'taskDescription': 'bla2', 'status': 'false'},
    'task3': {'task': 'build', 'taskDescription': 'bla3', 'status': 'false'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')
parser.add_argument('taskDescription')
parser.add_argument('status')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task'], 'taskDescription': args['taskDescription'], 'status': args['status']}
        TODOS[todo_id] = task
        return task, 201

    def post(self, todo_id):
        args = parser.parse_args()
        #todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        #todo_id = 'todo%i' % todo_id
        task = {'task': args['task'], 'taskDescription': args['taskDescription'], 'status': args['status']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)