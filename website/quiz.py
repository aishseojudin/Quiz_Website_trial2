from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

quiz = Blueprint('quiz', __name__)


@quiz.route("/",methods=["GET"])
def get_quiz():
    return render_template("quiz.html",a=1)