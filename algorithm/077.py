# 이항계수 구하기 2 (백준 11051)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

D = [[0 for j in range(N+1)] for i in range(N+1)]
dividend = 10007

for i in range(N+1):
    D[i][0] = 1
    D[i][1] = i
    D[i][i] = 1

for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = (D[i-1][j-1] + D[i-1][j]) % dividend

print(D[N][K] % dividend)