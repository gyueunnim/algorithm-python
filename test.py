import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

s = [0]
temp = 0

for i in numbers:
    temp += i
    s.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i - 1])
 