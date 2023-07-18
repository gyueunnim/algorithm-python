# 1
'''
korean, english, math = 80, 75, 55
total = korean + english + math
print(total / 3)
'''

# 2
'''
num = 13
if (num % 2) == 0:
    print("짝수")
else:
    print("홀수")
'''

# 3
'''
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
'''

# 4
'''
pin = "881120-1068234"
print(pin[7])
'''

# 5
'''
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)
'''

# 6
'''
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
'''

# 7
'''
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)
'''

# 8
'''
a = (1, 2, 3)
a = a + (4,)
print(a)
'''

# 9
# 생략

# 10
'''
a = {'A' : 90, 'B' : 80, 'C' : 70}
result = a.pop('B');
print(a)
print(result)
'''

# 11
'''
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)
'''

# 12
'''
a = b = [1, 2, 3]
a[1] = 4
print(b)
# a, b는 같은 주소를 가리키고 있다.
'''
'''
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(b)
'''