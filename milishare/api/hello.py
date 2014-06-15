from flask import Blueprint

bp = Blueprint('test', __name__)

@bp.route('/hello')
def hello():
    return "Hello World!"
