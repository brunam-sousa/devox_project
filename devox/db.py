#reference: https://flask.palletsprojects.com/en/latest/tutorial/database/
#used for tests only, will be replaced for a ORM framework (SQLAlchemy) 

#creating a connection with SQLite Database (closed before the response is sent)
import sqlite3

import click
#g is a special object that is unique for each request, will be used to store the DB connection
## at this way the connection is reused instead of be created again if "get_db" was called a second time
#"current_app" is a special object that points to the Flask application handling the request
from flask import current_app, g

def get_db():
    if 'db' not in g:
        # "sqlite3.connect()" establishes a connection to the file pointed at by the DATABASE configuration key
        g.db = sqlite3.connect(
            current_app.config['DATABASE'], # The path to the database file to be opened
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        #tells the connection to return rows that behave like dicts. This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



def init_db():
    # returns a database connection, used to execute the schema.sql
    db = get_db()
    # "open_resource()" opens a file relative to the devox package    
    with current_app.open_resource('schema.sql') as f:
        # 'executescript' execute a sql statements
        db.executescript(f.read().decode('utf8'))

# click.command() defines a command line command called init-db that calls
# the init_db function and shows a success message to the user.
# command: $ flask --app flaskr init-db
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


# registering the "close_db" and "init_db_command" functions with the application instance
def init_app(app):
    #tells Flask to call that function when cleaning up after returning the response
    app.teardown_appcontext(close_db)
    #adds a new command that can be called with the flask command
    app.cli.add_command(init_db_command)
