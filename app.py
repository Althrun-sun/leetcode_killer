from flask import Flask, render_template

app = Flask(__name__)
problems = [
    {
        'category': 'Linked List',
        'questions': ['Question 1', 'Question 2', 'Question 3']
    },
    {
        'category': 'Tree',
        'questions': ['Question 4', 'Question 5', 'Question 6']
    }
]

@app.route('/')
def index():
    return render_template('index.html',problems=problems)

if __name__ == '__main__':
    app.run(debug=True)
