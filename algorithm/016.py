# 버블 정렬 프로그램 1 (백준 1377)
import sys
input = sys.stdin.readline

n = int(input())
a = []

change = False
c = 0

for i in range(n):
    a.append((int(input()), i))

sorted_a = sorted(a) # 내장 sorted는 nlogn의 복잡도
max = 0

for i in range(n):
    if sorted_a[i][1] - i > max:
        max = sorted_a[i][1] - i

print(max+1)