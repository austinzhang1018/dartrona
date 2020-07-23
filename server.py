from flask import Flask
app = Flask(__name__)
from bot import get_prediction

@app.route('/', methods['POST'])
def question_answer():
    question = request.json['question']
    return get_prediction 
