# 1, 2
'''
class Calculator :
    def __init__(self) :
        self.value = 0
    def add(self, val) :
        self.value += val

class UpgradeCalculator(Calculator) :
    def minus(self, val) :
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


class MaxLimitCalculator(Calculator) :
    def add(self, val) :
        self.value += val
        if self.value > 100 :
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)
'''

# 3
'''
print(all([1, 2, abs(-3)-3])) # False
print(chr(ord('a')) == 'a') # True
'''

# 4
'''
a = list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
print(a)
'''

# 5
# print(int(0xea))

# 6
# print(list(map(lambda x: x * 3, [1, 2, 3, 4])))

# 7
# print(max([-8, 2, 7, 5, -3, 5, 0, 1]) + min([-8, 2, 7, 5, -3, 5, 0, 1]))

# 8
# print(round(17/3, 4))

# 12
'''
import random
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)
'''

# 14
'''
import operator
data = sorted(data, key=operator.itemgetter(1))
'''

# 15
'''
import itertools
data = ['나지혜', '성성민', '윤지현', '김정숙']
print(list(itertools.combinations(data, 2)))
'''

# 16
'''
import itertools
a = list(itertools.permutations("abcd", 4))
for i in a:
    print(''.join(i), end=' ')
'''

# 17
import random
import itertools

people = ['김승현', '김진호', '강춘자', '이예준', '김현주']
job = ['청소', '빨래', '설거지']
random.shuffle(people)
result = itertools.zip_longest(people, job, fillvalue="휴식")
for i in result :
    print(i)

# 18
'''
import math
a = math.gcd(200, 80)
n1 = 200 / a
n2 = 80 / a
print(a, n1*n2)
'''