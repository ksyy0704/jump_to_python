money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#비교 연산자
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#x in s, x not in s(s는 리스트, 튜플, 문자열)
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라.
pocket = ['paper', 'cellphone', 'money']
if 'card' not in pocket:
    print("걸어 가라")
else:
    print("버스를 타고 가라")

#조건문에서 아무 일도 하지 않게 설정
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")

pocket = ['papaer', 'cellphone']
care = True
if 'money' in pocket:   #주머니에 돈이 있으면
    print("택시를 타고 가라")
elif card:              #주머니에 돈이 없고 카드가 있으면
    print("택시를 타고 가라")
else:                   #주머니에 돈도 없고 카드도 없으면
    print("걸어 가라")

#조건부 표현식
score = 70
if score >=60:
    message = "success"
else:
    message = "failure"

#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
message = "success" if score >= 60 else "failure"
