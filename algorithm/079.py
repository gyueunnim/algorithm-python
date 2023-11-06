# 다리 놓기 (백준 1010)
import sys
input = sys.stdin.readline

T = int(input())

D = [[0 for _ in range(31)] for _ in range(31)]

for i in range(31):
    D[i][0] = 1
    D[i][i] = 1
    D[i][1] = i

for i in range(2 ,31):
    for j in range(1, i):
        D[i][j] = D[i-1][j-1] + D[i-1][j]

for _ in range(T):
    N, M = map(int, input().split())
    print(D[M][N])