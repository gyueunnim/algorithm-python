# 조약돌 꺼내기 (백준 13251)
import sys
input = sys.stdin.readline

M = int(input())
S = list(map(int, input().split()))
N = sum(S)
K = int(input())

D = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    D[i][0] = 1
    D[i][i] = 1
    D[i][1] = i

for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j-1] + D[i-1][j]

answer = 0
for i in range(M):
    answer += (D[S[i]][K] / D[N][K])

print(answer)