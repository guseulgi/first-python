"""
# 출력
print('Hello world!')

# 함수 선언
def say_hello() :
    print('Hello How R U?')

# 함수 호출
say_hello()

# 함수의 파라미터
def say_hello(name = 'anon') :
    print('Hello, '+ name+ " How R U?")

say_hello()
say_hello('Kim')
"""

# 계산기
# def plus(num1=0, num2=0):
#     return num1 + num2


# def minus(num1=0, num2=0):
#     return num1 - num2


# def multiple(num1=0, num2=0):
#     return num1 * num2


# def divide(num1=0, num2=1):
#     return num1 / num2


"""
# 조건문
password_correct = True
if password_correct:
    print('Correct')
else:
    print('Wrong')
  
winner = 10
if winner > 10:
    print('Winner is greater than 10')
elif winner < 10:
    print('Winner is less than 10')
else:
    print('Winner is 10')

# and / or
age = int(input('How old R U?'))
print('Your Age is', age)
if age < 18:
    print('You cant drink')
elif age >= 18 and age <= 35:
    print('You drink beer')
else:
    print('Go ahead!')

# 반복문 - 숫자 맞추기
from random import randint
playing = True
pc_choice = randint(1, 50)

while playing:
  user_choice = int(input('Choose number'))
  if user_choice == pc_choice:
      print('You won!')
      playing = False
  elif user_choice > pc_choice:
      print('Lower')
  elif user_choice < pc_choice:
      print('Higher')
"""
"""
# List
days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

# Tuple -> 불변성
nums = (1, 2, 3, 4, 5)
print(nums[-1]) # 5
print(nums[-3]) # 3

# Dictionary
player = {
    'name' : 'Kim',
    'age' : 22,
}
"""

# 웹 사이트의 유효성 검사 예제
# from requests import get
# websites = (
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
# )

# results = {}

# for web in websites:
#   if not web.startswith('https://'):
#     print('Fix')
#     web = f"https://{web}"
#   res = get(web)
#   if res.status_code == 200:
#      results[web] = 'OK'
#   else:
#      results[web] = 'Failed'

# print(results)

# Flask 사용

from flask import render_template # html 을 읽어오기 위한 함수
from flask import Flask, redirect
from flask import request
from extractors.indeed_teaching import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
app = Flask(__name__)
# 오류 방지용 __name__ 사용

# 임시 DB
db = {}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search')
def search():
    keyword = request.args.get('keyword')  # request.args 로 쿼리스트링을 읽어올 수 있음
    if keyword == None:
        return redirect('/')
    if keyword in db:
        jobs = db[keyword]
    else:
        # indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = wwr  # + indeed  # list 는 +로 합치는 것이 가능
    return render_template('search.html', keyword=keyword, jobs=jobs)
    # render_template() 함수의 파라미터에 넘겨줄 값을 넣어줘서 활용 가능


app.run("127.0.0.1", port=8000, debug=True)  # debug = True 면 수정할 때마다 새로고침 됨
