""" Making directory a package """
from flask import Flask

app = Flask(__name__)

from app import views
