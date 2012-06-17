from flask import Flask, g, abort
from flaskext.mongoalchemy import MongoAlchemy

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'library'
app.config.from_envvar('FIT_SETTINGS', silent = True)
app.debug = True
db = MongoAlchemy(app)

app.config['SECRET_KEY'] = 'development key'
import fiTracker.views
