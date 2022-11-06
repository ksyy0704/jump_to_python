#for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#다양한 for문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

#for문의 응용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

#for문과 continue문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

#for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a) #range(0,10) <- 0,1,2,3,4,5,6,7,8,9

a = range(1, 11) #<-1,2,3,4,5,6,7,8,9,10

add = 0
for i in range(1, 11):
    add = add + i

print(add)

for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

#for문과 range 함수를 사용하여 1부터 100까지 더하기
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)

#for와 range를 사용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

#리스트 내포 사용하기
#리스트 내포 : 리스트 안에 for문을 포함
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

#[표현식 for 항목 in 반복 가능 객체 if 조건]
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

#for문을 2개 이상 사용하는 것도 가능
#[표현식 for 항목1 in 반복 가능 객체1 if 조건1
#       for 항목2 in 반복 가능 객체2 if 조건2
#       ...
#       for 항목n in 반복 가능 객체n if 조건n]
result = [x * y for x in range(2, 10)
          for y in range(1, 10)]
print(result)