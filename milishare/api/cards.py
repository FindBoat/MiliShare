from datetime import datetime

from flask import Blueprint, abort, request

from ..services import cards
from . import route


bp = Blueprint('cards', __name__, url_prefix='/cards')


@route(bp, '/')
def query():
    """Returns a list of unexpired card instances ordered by create time.

    :param channel: (optional) The channel of the card.
    :param count: (optional) The # of cards returned. Default is 10.
    """
    channel = request.args.get('channel', None)
    count = request.args.get('count', 10)

    if channel:
        results = cards.find(channel=channel)
    else:
        results = cards.find(permanent=False)
    results = results.order_by(cards.__model__.create_time.desc()).limit(count).all()

    # Remove expired cards.
    fresh_cards = []
    for card in results:
        if _is_card_expired(card):
            cards.delete(card)
        else:
            fresh_cards.append(card)
    return fresh_cards

@route(bp, '/', methods=['POST'])
def create():
    channel = request.json.get('channel', None)
    if not channel or cards.first(channel=channel):
        print 'Channel %s already used' % channel
        abort(404)
    params = request.json
    params['create_time'] = datetime.now()
    params['permanent'] = False
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
