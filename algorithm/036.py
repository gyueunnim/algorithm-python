# 최솟값을 만드는 괄호 배치 찾기 (백준 1541)
import sys
input = sys.stdin.readline

A = list(map(str, input().split("-")))
B = []
C = []

answer = 0

for i in range(len(A)):
    B.append(list(map(int, A[i].split("+"))))

for i in B:
    total = 0
    while i:
        total += i.pop()
    C.append(total)

for i in range(len(C)):
    if i == 0:
        answer += C[i]
    else:
        answer -= C[i]

print(answer)    
