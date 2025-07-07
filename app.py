from flask import Flask, jsonify
import json
import random
from geometry.generator import generate_triangle_area_question

app = Flask(__name__)

with open('data/questions.json', 'r', encoding='utf-8') as f:
    QUESTION_BANK = json.load(f)

@app.route('/question/<subject>')
def get_question(subject):
    if subject == 'geometry':
        q = generate_triangle_area_question()
    else:
        questions = QUESTION_BANK.get(subject, [])
        if not questions:
            return jsonify({'error': 'subject not found'}), 404
        q = random.choice(questions)
    return jsonify(q)


if __name__ == '__main__':
    app.run(debug=True)
