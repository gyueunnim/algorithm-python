# 수열 (백준 2559) 실버3
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
A = list(map(int, input().split()))
S = []
max = 0
for i in range(D):
    max += A[i]
S.append(max)
    
R = N-D+1

for j in range(1, R):
    S.append(S[j-1] - A[j-1] + A[j+D-1])

print(sorted(S)[R-1])

'''
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
'''