# DFS와 BFS 프로그램 (백준 1260)
from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

nodeNum, edgeNum, startPoint = map(int, input().split())

# 인접리스트 생성
A = [[] for _ in range(nodeNum+1)]

# 방문리스트 생성
visited = [False] * (nodeNum+1)

# 큐
queue = deque()

for _ in range(edgeNum):
    node, edge = map(int, input().split())
    A[node].append(edge)
    A[edge].append(node)

for i in range(1, nodeNum+1):
    A[i].sort()

def DFS(v):
    print(v, end=" ")
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

DFS(startPoint)
print()

visited = [False] * (nodeNum+1)

def BFS(v):
    queue.append(v)
    visited[v] = True
    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for i in A[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

BFS(startPoint)