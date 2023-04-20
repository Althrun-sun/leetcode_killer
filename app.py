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
from leetcode import LeetcodeClient

def get_problem_url(title_slug, difficulty):
    lc_client = LeetcodeClient()
    problems = lc_client.get_problems()
    
    for problem in problems['stat_status_pairs']:
        if problem['stat']['question__title_slug'] == title_slug and problem['difficulty']['level'] == difficulty:
            problem_id = problem['stat']['question_id']
            return f"https://leetcode.com/problems/{title_slug}/"

    return None

# 示例：获取 "two-sum" 题目的 URL，难度为 1（简单）
url = get_problem_url("two-sum", 1)
print(url)






@app.route('/')
def index():
    return render_template('index.html',problems=problems)

if __name__ == '__main__':
    app.run(debug=True)
