from ..core import db
from ..helpers import JsonSerializer


class CardJsonSerializer(JsonSerializer):
    pass


class Card(CardJsonSerializer, db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer(), primary_key=True)
    channel = db.Column(db.String(50), unique=True)
    content = db.Column(db.Text())
    create_time = db.Column(db.DateTime())
    permanent = db.Column(db.Boolean(), default=False)
