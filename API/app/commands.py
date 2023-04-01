from flask.cli import with_appcontext
from app.extensions import db
from app.models import User, Card, Adress
import click


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Creating Database")
    db.drop_all()
    db.create_all()
    click.echo("Finished Creating Database")


@click.command("populate_db")
@with_appcontext
def populate_db():

    click.echo("nothing")
