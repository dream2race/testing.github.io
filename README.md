# AI Exam Generator Demo

This project provides a minimal demo of an AI-powered exam generator aimed at 11th-12th grade students in Lithuania. It generates multiple-choice questions with immediate feedback and simple progress tracking. Geometry questions include generated diagrams.

## Features

- **Multiple subjects**: example questions for math and history plus geometry generation.
- **Immediate feedback** with hints and correct answers.
- **Basic progress tracking** in the browser title.
- **Simple CSS animations** for a student-friendly interface.

## Running

Install the Python dependencies and start the server:

```bash
pip install -r requirements.txt
FLASK_APP=app.py flask run
```

Then open `index.html` in a browser and interact with the question generator.

The geometry endpoint provides images encoded in base64. This demo can be extended with more subjects and question types based on the NŠA curriculum.
