# 최대 공약수 구하기 (백준 1850)
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        return gcd(n2, n1%n2)

N = gcd(A, B)

for _ in range(N):
    print('1', end='')
print()