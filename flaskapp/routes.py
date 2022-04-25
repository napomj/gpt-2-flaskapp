from inspect import Parameter
from multiprocessing.sharedctypes import Value
from django.shortcuts import render
from flask import Blueprint, render_template, request, redirect
from .generator import ai

generator = Blueprint('generator', __name__)

@generator.route('/')
def index():
    # parameter = request.form['parameter']
    return render_template('index.html')

@generator.route('/textgen', methods=['POST'])
def textgen():
    title = request.form['title']
    temp = request.form['temp-input']
    length = request.form['length-input']
    model = request.form['model-input']
    try:
        temp = int(temp)
    except ValueError:
        temp = 1
    try:
        length = int(length)
    except ValueError:
        length = 200
    text = ai.generate_text(title, model, length, temp)

    return render_template('index.html', text=text)