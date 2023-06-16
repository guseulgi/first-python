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
from flask import render_template
from flask import Flask


def plus(num1=0, num2=0):
    return num1 + num2


def minus(num1=0, num2=0):
    return num1 - num2


def multiple(num1=0, num2=0):
    return num1 * num2


def divide(num1=0, num2=1):
    return num1 / num2


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

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', name='nico')


@app.route('/search')
def search():
    return render_template('search.html')


app.run(debug=True)
