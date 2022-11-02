#자료형의 값을 저장하는 공간, 변수

a = [1, 2, 3]
print(id(a))

#리스트를 복사할 때
b = a
print(a)
print(b)
print(id(a))
print(id(b))  #[1,2,3] 리스트를 참조하는 변수가 a 변수 1개에서 b 변수까지 추가되어 2개로 늘어남. a와 b가 가리키는 대상이 동일

print(a is b) #a와 b가 가리키는 객체가 동일한가? True

a[1] = 4
print(a)
print(b)  #a와 b가 가리키는 객체가 동일하기 때문에 a 리스트의 두 번째 요소만 바꿨지만 b도 똑같이 바뀜

#b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 하려면?
#[:] 사용
a = [1, 2, 3]
b = a[:] #리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
print(id(a))
print(id(b))
a[1] = 4
print(a)
print(b)

#copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(id(a))
print(id(b))
print(b is a)  #False

#변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print(a)
print(b)

(a, b) = 'python', 'life'
print(a)
print(b)

[a, b] = ['python', 'life']
print(a)
print(b)

a = b = 'python'
print(a)
print(b)

#두 변수의 값을 바꾸기
a = 3
b = 5
a, b = b, a
print(a)
print(b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  #False