# 이항계수 구하기 1 (백준 11050)
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# DP 테이블 선언
D = [[0 for j in range(N+1)] for i in range(N+1)]

# DP 테이블 초기화
for i in range(N+1):
    D[i][0] = 1
    D[i][1] = i
    D[i][i] = 1

for i in range(2, N+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j-1] + D[i-1][j]

print(D[N][K])