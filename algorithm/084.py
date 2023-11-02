# 정수를 1로 만들기 (백준 1463)
import sys
input = sys.stdin.readline

X = int(input())
D = [0] * (X+1)
D[1] = 0

for i in range(2, X+1):
    D[i] = D[i-1] + 1

    if i%2 == 0:
        D[i] = min(D[i], D[int(i/2)] + 1)
    if i%3 == 0:
        D[i] = min(D[i], D[int(i/3)] + 1)

print(D[X])