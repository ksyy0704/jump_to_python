odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2])
print(a[-1])  #문자열에서와 마찬가지로 마지막 요솟값

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])

#리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])  #문자열과 동일
print(a[:3])

#리스트 연산하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

#리스트 반복하기
print(a*3)

#리스트 길이 구하기
print(len(a))

#리스트의 수정과 삭제
a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]  #리스트 a에서 1번째 요솟값 삭제
print(a)

a = [1, 2, 3, 4, 5]
del a[:2]
print(a)

#리스트 관련 함수
#리스트에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5,6])
print(a)

#리스트 정렬
a = [1, 4, 3, 2]
a.sort()  #오름차순으로 정렬, 문자열 정렬도 가능
print(a)

#리스트 뒤집기
a = ['a', 'c', 'b']
a.reverse()
print(a)

#위치 반환
a = [1, 2, 3]
print(a.index(3))  #만약 리스트에 존재하지 않는 값의 위치를 찾고자 하면 오류 발생

#리스트에 요소 삽입
a.insert(0, 4)  #a[0]위치에 4 삽입
print(a)
a.insert(3, 5)  #a[3]위치에 5 삽입
print(a)

#리스트 요소 제거
a = [1, 2, 3, 1, 2, 3]
a.remove(3)  #리스트에서 첫번째로 나오는 해당 값에 해당하는 값을 삭제
print(a)

#리스트 요소 끄집어내기
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))  #pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제
print(a)

#리스트에 포함된 요소 x의 개수 세기
a = [1, 2, 3, 1]
print(a.count(1))
print(a.count(2))

#리스트 확장
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)