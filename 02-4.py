#리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

#튜플 인덱싱
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

#슬라이싱
print(t1[1:]) #t1[1]부터 튜플의 마지막 요소까지 슬라이싱

#튜플 더하기
t2 = (3, 4)
print(t1 + t2)

#튜플 곱하기
print(t2 * 3)

#튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
print(len(t1))

a = (1, 2, 3)
print(a + (4,))