# 트리 순회하기 (백준 1991)
import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = [left, right]

def preOrder(n):
    if n == '.':
        return
    print(n, end='')
    preOrder(tree[n][0])
    preOrder(tree[n][1])

def inOrder(n):
    if n == '.':
        return
    inOrder(tree[n][0])
    print(n, end='')
    inOrder(tree[n][1])

def postOrder(n):
    if n == '.':
        return
    postOrder(tree[n][0])
    postOrder(tree[n][1])
    print(n, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')

print(tree)