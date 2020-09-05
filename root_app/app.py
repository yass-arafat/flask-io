from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from root_app.models import User

from root_app import auth, api
from root_app.extensions import db, jwt, migrate, apispec


def create_app(testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask("root_app")
    app.config.from_object("root_app.config")

    # set optional bootswatch theme
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    admin = Admin(app, name='Flask Admin Panel', template_mode='bootstrap3')
    # Add administrative views here
    admin.add_view(ModelView(User, db.session))

    if testing is True:
        app.config["TESTING"] = True

    configure_extensions(app, cli)
    configure_apispec(app)
    register_blueprints(app)

    return app


def configure_extensions(app, cli):
    """configure flask extensions
    """
    db.init_app(app)
    jwt.init_app(app)

    if cli is True:
        migrate.init_app(app, db)


def configure_apispec(app):
    """Configure APISpec for swagger support
    """
    apispec.init_app(app, security=[{"jwt": []}])
    apispec.spec.components.security_scheme(
        "jwt", {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    )
    apispec.spec.components.schema(
        "PaginatedResult",
        {
            "properties": {
                "total": {"type": "integer"},
                "pages": {"type": "integer"},
                "next": {"type": "string"},
                "prev": {"type": "string"},
            }
        },
    )


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)
