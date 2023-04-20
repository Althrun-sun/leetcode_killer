import requests
from bs4 import BeautifulSoup

def get_problem_url(title_slug, difficulty):
    base_url = "https://leetcode.com"
    problems_url = f"{base_url}/api/problems/all/"

    response = requests.get(problems_url)
    if response.status_code == 200:
        problems = response.json()
        
        for problem in problems['stat_status_pairs']:
            if problem['stat']['question__title_slug'] == title_slug and problem['difficulty']['level'] == difficulty:
                problem_id = problem['stat']['question_id']
                return f"https://leetcode.com/problems/{title_slug}/"

    return None

# 示例：获取 "two-sum" 题目的 URL，难度为 1（简单）
url = get_problem_url("two-sum", 1)
print(url)
