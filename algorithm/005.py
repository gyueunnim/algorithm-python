# 나머지 합 구하기 (백준 10986)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
s = [0] * n
c = [0] * m
s[0] = numbers[0]
count = 0

for i in range(1, n):
    s[i] = s[i - 1] + numbers[i]

for i in s:
    temp = i % m
    if temp == 0:
        count += 1
    c[temp] += 1

for i in range(m):
    if c[i] > 1:
        count += c[i] * (c[i] - 1) // 2

print(count)