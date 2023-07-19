# 1010
'''
import math

t = int(input())
result = []

for _ in range(t) :
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    result.append(bridge)

for i in result :
    print(i)
'''

# 1094
'''
stickArray = [64]
X = int(input())
while True :
    if sum(stickArray) == X :
        break
    halfStick = min(stickArray) / 2
    stickArray.remove(min(stickArray))
    stickArray.extend([halfStick, halfStick])
    if sum(stickArray) - halfStick >= X :
        stickArray.remove(halfStick)

print(len(stickArray))
'''

# 1181
'''
n = int(input())
words = []
for i in range(n) :
    words.append(input())
words = list(set(words))
words.sort()
words.sort(key=len)
#words = sorted(words)
#words = sorted(words, key=lambda x: len(x))
for i in words :
    print(i)
'''

