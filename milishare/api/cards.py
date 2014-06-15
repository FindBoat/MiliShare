from datetime import datetime

from flask import Blueprint, abort, request

from ..services import cards
from . import route


bp = Blueprint('cards', __name__, url_prefix='/cards')


@route(bp, '/')
def query():
    """Returns a list of card instances."""
    channel = request.args.get('channel', None)
    if not channel:
        return cards.all()
    else:
        card = cards.first(channel=channel)
        if not card:
            return []

        # Check if card is expired.
        if _is_card_expired(card):
            cards.delete(card)
            return []
        else:
            return [card]


@route(bp, '/', methods=['POST'])
def create():
    channel = request.json.get('channel', None)
    if not channel or cards.first(channel=channel):
        print 'Channel %s already used' % channel
        abort(404)
    params = request.json
    print params
    params['create_time'] = datetime.now()
    return cards.create(**params)


def _is_card_expired(card):
    if card.permanent:
        return False
    if not card.create_time:
        return True
    d = datetime.now() - card.create_time
    if d.total_seconds() > 24 * 60 * 60:
        return True

    return False
