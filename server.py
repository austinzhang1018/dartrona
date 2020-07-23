from flask import Flask, redirect
app = Flask(__name__)

from flask_cors import CORS, cross_origin
from bot import get_prediction

cors = CORS(app)

@app.route('/', methods['GET'])
def index():
    return redirect('https://austinzhang1018.github.io/dartrona/')

@app.route('/api-qa', methods['POST'])
def question_answer():
    question = request.json['question']
    return get_prediction(question, 5, 5)
