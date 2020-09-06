import click
from flask.cli import FlaskGroup

from root_app.app import create_app


def create_root_app(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_root_app)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from root_app.extensions import db
    from root_app.models import User

    click.echo("create user")
    user = User(username="yarafat", email="yarafat@admin.com", password="yarafat", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
