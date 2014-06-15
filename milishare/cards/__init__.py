from ..core import Service, MiliShareError
from .models import Card


class CardsService(Service):
    __model__ = Card
