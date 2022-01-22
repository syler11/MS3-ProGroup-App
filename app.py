import os
from flask import (
    Flask, flash, render_template, url_for)
from flask_pymongo import pymongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)