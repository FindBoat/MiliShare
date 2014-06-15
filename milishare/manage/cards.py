from datetime import datetime

from flask import current_app
from flask.ext.script import Command, prompt

from ..services import cards


class CreateCardCommand(Command):
    def run(self):
        channel = prompt('channel')
        content = prompt('content')
        new_card = cards.create(
            channel=channel, content=content, create_time=datetime.now())
        print 'Card(id=%s, channel=%s, content=%s)' % (
            new_card.id, new_card.channel, new_card.content)


class DeleteCardCommand(Command):
    def run(self):
        id = prompt('id')
        card = cards.first(id=id)
        if not card:
            print 'Invalid card/'
        else:
            cards.delete(card)
            print 'Card deleted successfully.'


class ListCardsCommand(Command):
    def run(self):
        for card in cards.all():
            print '\n%s' % card.__dict__
