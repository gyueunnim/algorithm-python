# 특정 거리의 도시 찾기 (백준 18352)
from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

L = [[] for _ in range(N+1)]
Q = deque()
visited = [-1] * (N+1)
answer = []

for i in range(M):
    s, e = map(int, input().split())
    L[s].append(e)

count = 0

def BFS(v):
    Q.append(v)
    visited[v] += 1
    while Q:
        now_node = Q.popleft()
        for i in L[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                Q.append(i)

BFS(X)

for i in range(1, N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)