from flask import Flask, render_template, request

import boto3
import json

app = Flask(__name__)


def download_json_from_s3(bucket, key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    return json.loads(response['Body'].read().decode('utf-8'))


def upload_json_to_s3(json_data, bucket, key):
    s3 = boto3.client('s3')
    s3.put_object(
        Body=json.dumps(json_data),
        Bucket=bucket,
        Key=key
    )


def init_read_data():
    data = download_json_from_s3('leet-code-killer', 'data/problems_data.json')
    problems = data["problems"]
    problem_stat = data["problem_stat"]
    return problems, problem_stat


json_data = download_json_from_s3(
    'leet-code-killer', 'data/problems_data.json')


@app.route('/')
def index():
    problems, problem_stat = init_read_data()
    return render_template('index.html', problems=problems)


@app.route('/update_problem_status', methods=['POST'])
def update_problem_status():
    problem_id = int(request.form['id'])
    new_status = bool(request.form['status'])
    global json_data
    # Update the problem status
    for cat_index,problem_info in enumerate(json_data["problems"]):
        problem_list = problem_info["questions"]
        for q_index,problem in enumerate(problem_list):
            if problem['id'] == problem_id:
                json_data["problems"][cat_index]['questions'][q_index]['completed']=new_status
                break
    upload_json_to_s3(json_data, 'leet-code-killer', 'data/problems_data.json')
    return 'OK', 200
if __name__ == '__main__':
    app.run(debug=True)
