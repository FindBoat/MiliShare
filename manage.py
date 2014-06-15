from flask.ext.script import Manager

from milishare.frontend import create_app
from milishare.manage import CreateCardCommand, DeleteCardCommand, ListCardsCommand


manager = Manager(create_app())
manager.add_command('create_card', CreateCardCommand())
manager.add_command('delete_card', DeleteCardCommand())
manager.add_command('list_cards', ListCardsCommand())


if __name__ == "__main__":
    manager.run()
