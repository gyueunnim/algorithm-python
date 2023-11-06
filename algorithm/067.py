# 트리의 부모 찾기 (백준 11725)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
L = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

for i in range(2, N+1):
    n1, n2 = map(int, input().split())
    L[n1].append(n2)
    L[n2].append(n1)

def DFS(v):
    visited[v] = True
    for i in L[v]:
        if not visited[i]:
            answer[i] = v
            DFS(i)

DFS(1)

for i in range(2, N+1):
    print(answer[i])