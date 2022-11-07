#파일 읽고 쓰기

#파일 생성하기
#파일 객체 = open(파일 이름, 파일 열기 모드)
f = open("새파일.txt", 'w')
f.close()

#파일을 쓰기 모드로 열어 출력값 적기
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
#readline 함수 사용하기
f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#readlines 함수 사용하기
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#read 함수 사용하기
f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

#파일에 새로운 내용 추가하기
#쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다.
#추가 모드('a')로 파일을 열면 원래 있던 값을 유지하면서 단지 새로운 값만 추가할 수 있다.
f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

#with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")   #with 블록을 벗어나는 순간 자동으로 close된다.