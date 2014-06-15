from flask import Blueprint, render_template


bp = Blueprint('homepage', __name__)


@bp.route('/')
@bp.route('/<channel>')
def index(channel=None):
    return render_template('index.html')
