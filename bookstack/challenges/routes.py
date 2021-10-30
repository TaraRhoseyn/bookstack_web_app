from flask import (
    Blueprint, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bookstack import mongo

reviews = Blueprint('challenges', __name__)