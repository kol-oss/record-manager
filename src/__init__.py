from flask import Flask

# Initialize HTTP server
app = Flask(__name__)

from src.controller import *
