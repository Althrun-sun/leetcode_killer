import openai
from flask import Flask, render_template, request, redirect, url_for
import hashlib
import boto3
import json

app = Flask(__name__)

aws_access_key_id="AKIA5GN6ERUHNZHMVFX7"
aws_secret_access_key="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"
def download_json_from_s3(bucket, key):

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    # s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    return json.loads(response['Body'].read().decode('utf-8'))


def upload_json_to_s3(json_data, bucket, key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    # s3 = boto3.client('s3')
    s3.put_object(
        Body=json.dumps(json_data),
        Bucket=bucket,
        Key=key
    )


json_data = download_json_from_s3(
    'leetcode-killer-1', 'data/problems_data.json')


@app.route('/')
def index():
    problems = json_data["problems"]
    problem_stat = json_data['problem_stat']
    return render_template('index.html', problems=problems, problem_stat=problem_stat)


@app.route('/update_problem_status', methods=['POST'])
def update_problem_status():
    problem_id = int(request.form['id'])
    new_status = True if request.form['status'] == 'true' else False
    global json_data
    # Update the problem status
    for cat_index, problem_info in enumerate(json_data["problems"]):
        problem_list = problem_info["questions"]
        curr_cat = problem_info["category"]
        for q_index, problem in enumerate(problem_list):
            if problem['id'] == problem_id:
                # print(problem,new_status)
                json_data["problems"][cat_index]['questions'][q_index]['completed'] = new_status
                if not new_status and json_data["problem_stat"][curr_cat]['completed'] > 0:
                    json_data["problem_stat"][curr_cat]['completed'] -= 1
                else:
                    json_data["problem_stat"][curr_cat]['completed'] += 1
                break
    new_data = data = download_json_from_s3(
        'leetcode-killer-1', 'data/problems_data.json')
    # print('new_data',new_data["problems"][0]['questions'][0]['completed'])
    upload_json_to_s3(json_data, 'leetcode-killer-1', 'data/problems_data.json')
    return 'OK', 200


@app.route('/reset_progress', methods=['POST'])
def reset_progress():
    global json_data
    reset_data = json_data
    # reset the problem status
    for cat_index, problem_info in enumerate(reset_data["problems"]):
        problem_list = problem_info["questions"]
        for q_index, problem in enumerate(problem_list):
            reset_data["problems"][cat_index]['questions'][q_index]['completed'] = False

    upload_json_to_s3(reset_data, 'leetcode-killer-1',
                      'data/problems_data.json')
    json_data = download_json_from_s3(
        'leetcode-killer-1', 'data/problems_data.json')
    return 'ok', 200


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # s3 = boto3.client('s3')
        s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        
        s3.put_object(
            Body=json.dumps({'username': username, 'pwd': hashed_password}),
            Bucket='leetcode-killer-1',
            Key="users/"+username+".json"
        )

        return redirect(url_for('index'))
    else:
        return render_template('register.html')


def check_password(username, password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    try:
        login_data = download_json_from_s3(
            'leetcode-killer-1', 'users/'+username+'.json')
        stored_password = login_data['pwd']
    except Exception as e:
        return False

    return hashed_password == stored_password


@app.route('/login', methods=['GET', 'POST'])
def login():
    invalid_login = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if check_password(username, password):
            return redirect(url_for('index'))
        else:
            invalid_login = True

    return render_template('login.html', invalid_login=invalid_login)


openai.organization = "org-TONaHPuXZEzb15vTUf5Yl8UK"
openai.api_key = "sk-3dqAbcK9p2EluYdd8L56T"+"3BlbkFJLUUJczsonN4lUpsvkOuH"


def generate_text(title):
    prompt = "please show the code to solve the python leetcode problem whose name is exctly:" +\
        title+"."+" And give some brief explaination about this alogrithm for the new learner." +\
        "Time and splace complexity should be included in explain part" +\
        "The explanation should be no more than 150 words." +\
        """Please note the python code format, please output the python code in its entirety 
        so that I can be recognized directly when I print your string, i.e. your output should include line breaks and spaces.
        """ +\
        """please just out like this:
        @ code 
        ...
        @ Explanation
        ...
        .""" +\
        "Be sure to add @ before code,and @ before Explanation not '#',also All lines are indented at the beginning because there is a class Solution further up."
    response = openai.ChatCompletion.create(
        
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a talented programmer specialized in solving LeetCode problems."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=350,
        n=1,
        temperature=0.1,
    )
    

    return response.choices[0].message['content'].strip()
def get_data(title):
    generated_text = generate_text(title)
    splietd_data = generated_text.split('@')
    code_text = splietd_data[1]
    explaine_txt = splietd_data[2]
    func_text = code_text.split('class Solution:')
    func_text = ''.join(func_text[1:])
    return func_text,explaine_txt


@app.route('/solution', methods=['GET', 'POST'])
def solution():
    title = request.args.get('title', None)
    if request.method == 'POST':
        pass
    else:
        func_text,explaine_txt=get_data(title)
        return render_template('solution.html', title=title, code_text=func_text, explaine_txt=explaine_txt)


if __name__ == '__main__':
    app.run()
