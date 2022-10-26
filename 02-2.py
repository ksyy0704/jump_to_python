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