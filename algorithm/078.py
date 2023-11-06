# 부녀회장이 될 테야 (백준 2775)
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    D = [[0 for j in range(n+1)] for i in range(k+1)]
    
    for i in range(n+1):
        D[0][i] = i
    
    for i in range(1, k+1):
        for j in range(1, n+1):
            D[i][j] = D[i][j-1] + D[i-1][j]

    print(D[k][n])