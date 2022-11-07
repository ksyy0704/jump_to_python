#함수
def add(a, b):  #a, b는 매개변수
    return a + b

a = 3
b = 4
c = add(a, b)
print(c)
print(add(3, 4))    #3, 4는 인수

#입력값과 결괏값에 따른 함수의 형태
#결괏값을 받을 변수 = 함수 이름(입력 인수 1, 입력 인수 2, ...)

#입력값이 없는 함수
#결괏값을 받을 변수 = 함수 이름()
def say():
    return 'Hi'

a = say()
print(a)

#결괏값이 없는 함수
#함수 이름(매개변수1, 매개변수2)
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

add(3, 4)
a = add(3, 4)
print(a)    #결괏값이 없기 때문에 None 출력

#입력값도 결괏값도 없는 함수
#함수 이름()
def say():
    print('Hi')
say()

#매개변수 지정하여 호출하기
def add(a, b):
    return a+b

result = add(a=3, b=7)  #a에 3, b에 7을 전달
print(result)

result = add(b=5, a=3)
print(result)

#여러 개의 입력값을 받는 함수 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

#키워드 파라미터
def print_kwargs(**kwargs):     #매개변수 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name="foo", age=3)

#함수의 결괏값은 언제나 하나이다.
def add_and_mul(a, b):
    return a+b, a*b     #튜플값 하나인 (a+b, a*b)로 돌려줌.

result = add_and_mul(3, 4)
print(result)
result1, result2 = add_and_mul(3, 4)

print(result1)
print(result2)

#return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return      #함수를 빠져나가는 역할
    print("나의 별명은 %s입니다." % nick)

say_nick("바보")
say_nick("야호")

#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):    #초기화시키고 싶은 매개변수는 항상 뒤쪽에!
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, False)

#함수 앞에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

#함수 안에서 함수 박의 변수를 변경하는 방법
#return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

#gloal 명령어 사용하기
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)    #가급적 global 명령어 사용보다는 return을 사용할 것

#lambda
#lambda 매개변수1, 매개변수2, ... : 매개변수를 사용한 표현식
add = lambda a, b: a + b
result = add(3, 4)
print(result)