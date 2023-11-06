# 리프 노드의 개수 구하기 (백준 1068)
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
visited = [False] * N
L = [[] for _ in range(N)]
count = 0
A = list(map(int, input().split()))

for i in range(N):
    if A[i] != -1:
        L[i].append(A[i])
        L[A[i]].append(i)
    else:
        root = i

def DFS(v):
    global count
    visited[v] = True
    sibling = False
    for i in L[v]:
        if not visited[i] and i != remove:
            sibling = True
            DFS(i)
    if not sibling:
        count += 1

remove = int(input())

if remove == root:
    print(0)
else:
    DFS(root)
    print(count)