# 오큰수 구하기 (백준 17298)
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
answer = [0] * n

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        answer[stack.pop()] = a[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

for i in range(n):
    print(answer[i], end=' ')
print()