#q1
a = 80
b = 75
c = 55
avg = (a + b + c)/3
print(avg)

#q2
#나머지 연산자를 사용
if ((13 % 2) == 0):
    print("13은 짝수")
else:
    print("13은 홀수")

#q3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

#q4
print(pin[7])

#q5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

#q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#q7
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

#q8
a = (1, 2, 3)
a = a + (4,)
print(a)

#q9
a = dict
#3번, 딕셔너리의 Key로는 변하는 값을 사용할 수 없기 때문에 리스트는 Key로 사용할 수 없다.

#q10
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

#q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
#a와 b가 가리키는 객체가 동일하기 때문에 a 리스트의 첫번째 요소의 값만 변경해도 b도 함께 변경된다.