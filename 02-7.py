#불 자료형

a = True
b = False

print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)

'''
문자열 
- "python"  참
- ""        거짓
리스트
- [1,2,3]   참
- []        거짓
튜플
- ()        거짓
딕셔너리
- {}        거짓
숫자형
- 0이 아닌 숫자  참
- 0            거짓
None        거짓
'''

#불 연산
print(bool('python'))

print(bool(''))
print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))