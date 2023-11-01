# 연결 요소의 개수 구하기 (백준 11724)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

# 인접 리스트
A = [[] for _ in range(n+1)]

# 방문 리스트
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)