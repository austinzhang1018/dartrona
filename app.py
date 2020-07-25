from flask import Flask, redirect, request
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

from bot import get_prediction


@app.route('/', methods=['GET'])
def index():
    return redirect('https://austinzhang1018.github.io/dartrona/')

@app.route('/api-qa', methods=['POST'])
def question_answer():
    print(request.get_data())
    question = request.json['question']
    return get_prediction(question, 5, 5)
