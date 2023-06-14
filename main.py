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

# 계산기
def plus(num1 = 0, num2 = 0):
    return num1 + num2
def minus(num1 = 0, num2 = 0):
    return num1 - num2
def multiple(num1 = 0, num2 = 0):
    return num1 * num2
def divide(num1 = 0, num2 = 1):
    return num1 / num2

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

    