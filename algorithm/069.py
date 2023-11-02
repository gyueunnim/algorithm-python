# 문자열 찾기 (백준 14429)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

textList = set([input() for _ in range(N)])
count = 0

for _ in range(M):
    checktext = input()
    if checktext in textList:
        count += 1

print(count)