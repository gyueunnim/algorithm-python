# 자료형
# 숫자형
'''
// : 몫
%  : 나머지
** : 제곱
'''

# 문자열 자료형
'''
문자열 합, 곱
문자열 인덱싱 : a[0], a[1], a[-1] 등
문자열 슬라이싱 : a[:4], a[17:-4] 등
문자열 포메팅 
1) 숫자, 문자열 바로 대입 : "I eat %s apples" % "five"
2) 변수로 대입
3) 2개 이상의 값 넣기 : "I eat %s apples and I sick for %s days" % ("five", num)
4) format 함수 사용 
- 숫자, 문자열 바로 대입 : "I eat {0} apples".format("five")
- 2개 이상의 값 넣기 : "I eat {0} apples and I sick for {1} days".format("five", num)
- 이름으로 넣기 : "I eat {num1} apples and I sick for {num2} days".format(num1 = 1, num2 = 2) # 반드시 name=value와 같은 형식이 필요함, 혼용도 가능
5) 정렬
- 왼쪽 정렬 : "{:<10}".format("hi")
- 오른쪽 정렬 : "{:>10}".format("hi")
- 가운데 정렬 : "{:^10}".format("hi")
- 공백 채우기 : "{:=^10}".format("hi"), "{:!^10}".format("hi")
- 소수점 표현 : "{:0.4f}".format(3.42134234)
6) f 문자열 포매팅 
- f"나의 이름은 {name}입니다. 나이는 {age+1}입니다."
- f"나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다." # d는 dictionary
- 정렬 : f"{'hi':=^10}"
문자열 관련 함수
len(string) : 문자열 길이
string.count(char) : 문자 개수 세기
string.find(char) : 문자 위치 알려주기
string.index(char) : 문자 위치 알려주기
char.join(string) : 문자열 삽입
string.strip() : 공백 지우기
string.replace("string1", "string2") : 문자열 바꾸기
string.split() : 문자열 나누기

예시 
print('Hello', 'Easy', 'Python', sep=', ')
print('Hello', 'Easy', 'Python', sep=', ', end='--')
print('Hello', end='\n\n') # 기본값은 \n임
print('Easy', end='--')
print('Python')

'''

# 리스트
'''
del
append() : 리스트 요소 추가
sort() : 리스트 정렬
reverse() : 리스트 뒤집기
index() : 인덱스 반환
insert() : 요소 삽입
remove() : 리스트 요소 제거
pop() : 리시트 요소 끄집어 내기 (맨 마지막 요소)
count() : 포함된 요소 세기
extend() : 리스트 확장 
'''

# 튜플 : 리스트와 거의 같다
'''
차이점 
- 튜플 () vs 리스트 []
- 튜플 : 요솟값 수정 불가능 vs 리스트 : 요솟값 수정 가능
'''

# 딕셔너리 자료형 : key-value 쌍
'''
# dic = {'name' : 'Gildong', 'phone' : '010-1234-5678', 'birth' : '0123'}
# a = {1: 'hi'}, a = {'a' : [1, 2, 3]}
a['name'] = "Hong" : 딕셔너리 쌍 추가

a.keys() : key 리스트 만들기 -> list(a.keys())를 통해 dict_keys 객체를 리스트로 변한 가능
a.values() : value 리스트 만들기 -> dict_values 객체 리턴
a.items() : key, value 쌍 얻기 -> dict_items 객체 리턴
a.clear() : key, value 쌍 모두 지우기
a.get('name') : key로 value 얻기 -> a.get('nokey', 'foo')를 할 경우 키가 없으면 foo 리턴
'name' in a : 해당 key가 딕셔너리 안에 있는지 조사
'''

# 집합 자료형
'''
set 키워드를 사용해 생성
s1 = set([1, 2, 3]), s2 = set("Hello")
특징 : set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환한 후 해야한다.
- 중복을 허용하지 않는다.
- 순서가 없다.
s1 & s2 : 교집합 (s1.intersection(s2))
s1 | s2 : 합집합 (s1.union(s2))
s1 - s2 : 차집합 (s1.difference(s2))
s1.add() : 값 1개 추가
s1.update() : 값 여러개 추가
s1.remove() : 특정 값 제거
'''

# bool 자료형
'''
bool() : 참 거짓
if [1, 2, 3] -> True
'''

# 변수 다루기 
# type() : 클래스 알려줌
# id() : 주소값 알려줌
# a is b : a와 b가 가리키는 객체가 같을까
'''
b = a를 할 경우 같은 주소를 가리킨다.
b = a[:]를 할 경우 값만 복사된다.
from copy import copy를 사용해 b = copy(a)를 해도 좋다
리스트의 자체 함수인 b = a.copy()를 사용해도 좋다
a, b = ('python', 'c')
(a, b) = 'python', 'c'
a = b = 'python'
a, b = b, a # 두 값을 바꿈
'''

# in, not in 연산자
'''
1 in [1, 2, 3]
2 not in [1, 3, 5]
'''

# pass : 조건문에서 아무 동작하지 않음
'''
pocket = ['money', 'phone']
if 'money' in pocket:
    pass
'''

# list comprehension
'''
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
'''