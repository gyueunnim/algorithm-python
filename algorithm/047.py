# 효율적으로 해킹하기 (백준 1325)
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = [[] for _ in range(N+1)]
trust = [0] * (N+1)

for _ in range(M):
    A, B = map(int, input().split())
    L[A].append(B)

def BFS(v):
    Q = deque()
    Q.append(v)
    visited[v] = True
    while Q:
        n = Q.popleft()
        for i in L[n]:
            if not visited[i]:
                visited[i] = True
                trust[i] += 1
                Q.append(i)

for i in range(1, N+1):
    visited = [False] * (N+1)
    BFS(i)

answer = 0
for i in range(1, N+1):
    answer = max(answer, trust[i])
# answer = max(trust) # max의 시간복잡도는 O(n)으로 좋은 편은 아니다.

for i in range(1, N+1):
    if answer == trust[i]:
        print(i, end=' ')
print()