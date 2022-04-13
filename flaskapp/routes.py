from inspect import Parameter
from django.shortcuts import render
from flask import Blueprint, render_template, request, redirect
from .generator import ai

generator = Blueprint('generator', __name__)

@generator.route('/')
def index():
    # parameter = request.form['parameter']
    return render_template('index.html')

@generator.route('/analyze', methods=['POST'])
def analyze():
    title = request.form['title']
    text = ai.generate_text(title)

    return render_template('index.html', text=text)