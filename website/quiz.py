from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

quiz = Blueprint('quiz', __name__)

def get_quiz_object():
    with open("quiz.json","r") as fp:
        print(fp.read())

@quiz.route("/",methods=["GET"])
@login_required
def get_quiz():
    # get_quiz_object()
    quiz_array = []
    return render_template("quiz.html",user=current_user,quiz=quiz_array)