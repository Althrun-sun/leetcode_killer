from flask import Flask, render_template, request ,redirect, url_for
import hashlib
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

json_data = download_json_from_s3('leet-code-killer', 'data/problems_data.json')


@app.route('/')
def index():
    problems=json_data["problems"]
    problem_stat=json_data['problem_stat']
    return render_template('index.html', problems=problems,problem_stat=problem_stat)


@app.route('/update_problem_status', methods=['POST'])
def update_problem_status():
    problem_id = int(request.form['id'])
    new_status = True if  request.form['status']=='true' else False
    global json_data
    # Update the problem status
    for cat_index,problem_info in enumerate(json_data["problems"]):
        problem_list = problem_info["questions"]
        curr_cat=problem_info["category"]
        for q_index,problem in enumerate(problem_list):
            if problem['id'] == problem_id:
                # print(problem,new_status)
                json_data["problems"][cat_index]['questions'][q_index]['completed']=new_status
                if not new_status and json_data["problem_stat"][curr_cat]['completed']>0:
                    json_data["problem_stat"][curr_cat]['completed']-=1
                else:
                    json_data["problem_stat"][curr_cat]['completed']+=1
                break
    new_data=data = download_json_from_s3('leet-code-killer', 'data/problems_data.json')
    # print('new_data',new_data["problems"][0]['questions'][0]['completed'])
    upload_json_to_s3(json_data, 'leet-code-killer', 'data/problems_data.json')
    return 'OK', 200
@app.route('/reset_progress', methods=['POST'])
def reset_progress():
    global json_data
    reset_data=json_data
    # reset the problem status
    for cat_index,problem_info in enumerate(reset_data["problems"]):
        problem_list = problem_info["questions"]
        for q_index,problem in enumerate(problem_list):
            reset_data["problems"][cat_index]['questions'][q_index]['completed']=False

    upload_json_to_s3(reset_data, 'leet-code-killer', 'data/problems_data.json')
    json_data = download_json_from_s3('leet-code-killer', 'data/problems_data.json')
    return 'ok',200

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 在此处处理表单提交和用户注册
        username = request.form['username']
        password = request.form['password']

        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        s3 = boto3.client('s3')
        s3.put_object(
        Body=json.dumps({'username':username,'pwd':hashed_password}),
        Bucket='leet-code-killer',
        Key="users/"+username+".json"
        )


        return redirect(url_for('index'))
    else:
        # 显示注册表单
        return render_template('register.html')

def check_password(username, password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    try:
        login_data = download_json_from_s3('leet-code-killer', 'users/'+username+'.json')
        stored_password=login_data['pwd']
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



    

if __name__ == '__main__':
    app.run(debug=True)
