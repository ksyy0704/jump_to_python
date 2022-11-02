#딕셔너리 쌍 추가, 삭제
a = {1: 'a'}
a[2] = 'b'  #{2:'b'} 쌍 추가
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3]
print(a)

del a[1]
print(a)

#딕셔너리에서 Key를 사용해 Value 얻기
grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

dic = {'name' : 'pey', 'phone': '0119993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#딕셔너리 만들 때 주의사항
a = {1: 'a', 1: 'b'}  #1이라는 Key 값이 중복으로 사용
print(a)  #1:'a' 쌍이 무시됨
#리스트를 키 값으로 사용할 수 없음.

#Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)

print(list(a.keys()))

#Value 리스트 만들기(values)
print(a.values())

#Key, Value 쌍 얻기(items)
print(a.items())

#Key, Value 쌍 모두 지우기(clear)
a.clear()
print(a)

#Key로 Value 얻기(get)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('nokey'))
print(a.get('foo', 'bar'))  #딕셔너리에 'foo'에 해당하는 값이 없다면 default 값인 'bar'를 돌려줌

#해당 Key가 딕셔너리 안에 있는지 조사(in)
print('name' in a)
print('email' in a)

##
dic = {'name': '홍길동', 'birth': 1128, 'age': 30}