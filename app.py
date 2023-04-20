from flask import Flask, render_template
import json
app = Flask(__name__)

with open("./data/problems_data.json", "r") as f:
    data = json.load(f)
    problems_with_details = data["problems_with_details"]
    problem_stat = data["problem_stat"]
problems=[{'category': key,'questions':value} for key,value in problems_with_details.items()]



@app.route('/')
def index():
    return render_template('index.html',problems=problems)

if __name__ == '__main__':
    app.run(debug=True)
