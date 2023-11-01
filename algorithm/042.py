# 최소 공배수 구하기 (백준 1934)
import sys
input = sys.stdin.readline

N = int(input())
A = []

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(N):
    print(int(A[i][0] * A[i][1] / gcd(A[i][0], A[i][1])))