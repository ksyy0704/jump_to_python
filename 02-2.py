food = "Python's favorite food is perl" #큰따옴표 안에 들어 있는 작은 따옴표는 문자열을 나타내기 위한 기호로 인식되지 않음.
print(food)

say = '"Python is very easy." he says' #문자열에 큰따옴표를 포함시키려면 작음따옴표로 둘러싸면 된다.
print(say)

#백슬래시(\)를 사용하여 문자열에 큰따옴표나 작은따옴표를 포함시킬 수도 있다.
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says"
print(food)
print(say)

#여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = "Life is too short\nYou need python" #줄을 바꾸는 이스케이프 코드 '\n' 삽입
print(multiline)

multiline = '''
Life is too short
You need python
''' #'''이나 """ 둘다 됨
print(multiline)

#문자열 연산하기
#문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)

#문자열 곱하기
a = "Python"
print(a * 2)

#문자열 곱하기 응용
print("=" * 50)
print("My program")
print("=" * 50)

#문자열 길이 구하기
a = "Life is too short"
print(len(a))

#문자열 인덱싱
a = "Life is too short, You need Python"
print(a[3])  #파이썬은 0부터 숫자를 센다.
print(a[-1]) #뒤에서부터 첫번째 문자

#문자열 슬라이싱
b = a[0] + a[1] + a[2] + a[3]
print(b) #Life 부분만 슬라이싱
print(a[0:4]) #슬라이싱 기법으로 a[시작 번호: 끝 번호] 지정시 끝 번호에 해당하는 것은 포함하지 않음.
print(a[19:]) #끝 번호 부분 생략하면 시작 번호부터 그 문자열의 끝까지를 뽑아냄.
print(a[:17]) #시작 번호 부분 생략하면 문자열의 처음부터 끝 번호까지 뽑아냄.
print(a[:]) #시작 번호와 끝 번호 모두 생략하면 문자열 전체를 뽑아냄.
print(a[19:-7]) #a[19]에서부터 a[-8]까지를 의미

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)
year = a[:4]
day = a[4:8]
print(year)
print(day)
print(weather)

#문자열 포맷팅
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day))

print("Error is %d%%." % 98)

#정렬과 공백
print("%10s" % "hi")  #hi를 오른쪽으로 정렬하고 나머지는 공백으로 채움
print("%-10sjane" % "hi")   #hi를 왼쪽으로 정렬하고 나머지는 공백으로 채움

#소수점 표현하기
print("%0.4f" % 3.42134234)  #소수점 아래 네번째 자리까지만 표시
print("%10.4f" % 3.42134234) #소수점 아래 네번째 자리까지만 표시하는데 전체 길이가 10개인 문자열 공간에서 오른쪽 정렬

#format 함수를 사용한 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} appels".format("five"))
number = 3
print("I eat {0} apples".format(number))
number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days.".format(number, day))
print("I eat {number} apples. so I was sick for {day} days.". format(number=10, day=3))
print("I eat {0} apples. so I was sick for {day} days.".format(10, day=3))
print("{0:<10}".format("hi"))  #문자열의 총 자릿수는 10자리, 왼쪽 정렬
print("{0:>10}".format("hi"))  #문자열의 총 자릿수는 10자리, 오른쪽 정렬
print("{0:^10}".format("hi"))  #가운데 정렬

#공백 채우기
print("{0:=^10}".format("hi"))  #공백은 =으로 채우고 가운데 정렬
print("{0:!<10}".format("hi"))  #공백은 !으로 채우고 왼쪽 정렬

#소수점 표현하기
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

#{ 또는 } 문자 표현하기
print("{{ and }}".format())

#f문자열 포매팅
name = "홍길동"
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

#문자열 관련 함수
#문자 개수 세기
a = "hobby"
print(a.count('b'))
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))  #찾는 문자나 문자열이 존재하지 않는다면 -1 반환

a = "Life is too short"
print(a.index('t'))  #문자열에 존재하지 않는 문자를 찾으면 오류 발생한다.

#문자열 삽입
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))

#소문자를 대문자로 바꾸기
a = "hi"
print(a.upper())

#대문자를 소문자로 바꾸기
b = a.upper()
print(b.lower())

#왼쪽 공백 지우기
a = " hi "
print(a.lstrip())

#오른쪽 공백 지우기
print(a.rstrip())

#양쪽 공백 지우기
print(a.strip())

#문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#문자열 나누기
print(a.split())  #공백 기준으로 문자열 나눔
b = "a:b:c:d"
print(b.split(":"))  # : 기준으로 문자열 나눔