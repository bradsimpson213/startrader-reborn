from flask import Flask, request, redirect
from .config import Config
from .models import db
from .routes import users, ships, transactions
from .seeds import seed_commands
from flask_migrate import Migrate
from flask_cors import CORS
import os

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
app.cli.add_command(seed_commands)

app.register_blueprint(users)
app.register_blueprint(ships)
app.register_blueprint(transactions)

# Application Security
CORS(app)               



@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)
            

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')



