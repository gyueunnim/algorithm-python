# 구간 합 구하기 2 (백준 11660)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0] * (n + 1)]
s = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    temp = [0] + [int(x) for x in input().split()]
    a.append(temp)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])


# 답안
'''
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0] * (n + 1)]
D = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(result)
    '''