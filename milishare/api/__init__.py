from functools import wraps

from flask import jsonify

from .. import factory
from ..helpers import JSONEncoder


def create_app(settings_override=None):
    app = factory.create_app(__name__, __path__, settings_override)

    # Set the default JSON encoder
    app.json_encoder = JSONEncoder

    return app

def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            sc = 200
            rv = f(*args, **kwargs)
            if isinstance(rv, tuple):
                sc = rv[1]
                rv = rv[0]
            return jsonify(dict(data=rv)), sc
        return f

    return decorator
