from sqlite3 import Error

from todo.commands.base import Command
from todo.renderers import RenderOutput


class Complete(Command):
    def run(self, id):
        try:
            todo = self._get_todo_or_raise(id)
            self.service.todo.complete(todo[0])

            RenderOutput("{bold}{green}✓ {reset}{bold}{todo_id}{reset}: {name}").render(todo_id=todo[0], name=todo[2])
        except Error as e:
            print('[*] Could not complete a todo due to "{}"'.format(e))
