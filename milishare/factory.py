from flask import Flask
from .core import db
from .helpers import register_blueprints
from .middleware import HTTPMethodOverrideMiddleware

def create_app(package_name, package_path, settings_override=None,
               register_security_blueprint=True):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the Overholt platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    :param register_security_blueprint: flag to specify if the Flask-Security
                                        Blueprint should be registered. Defaults
                                        to `True`.
    """
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('milishare.settings')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    # SQLAlchemy instance.
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()

    register_blueprints(app, package_name, package_path)

    app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

    return app
