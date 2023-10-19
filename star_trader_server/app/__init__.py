from flask import Flask, render_template
# from flask_cors import CORS
from .config import Config
from .models import db
from .routes import users, ships, transactions
from flask_migrate import Migrate


app = Flask(__name__)
# CORS(app, origins=["https://startrader-app.herokuapp.com", "https://localhost:5000", "http://startrader-app.herokuapp.com"])
app.config.from_object(Config)

app.register_blueprint(users)
app.register_blueprint(ships)
app.register_blueprint(transactions)

db.init_app(app)
migrate = Migrate(app, db)

