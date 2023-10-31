# 원하는 정수 찾기 (백준 1920)
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    # 이진 탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
'''
내 풀이
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

s = int(input())
Search = list(map(int, input().split()))

A.sort()

def binary_Search(left, right, n):
    if left > right:
        print(0)
        return
        
    center = int((left + right) / 2)

    if i < A[center]:
        binary_Search(left, center-1, i)
    elif i > A[center]:
        binary_Search(center + 1, right, i)
    else:
        print(1)
        return

left = 0
right = n-1

for i in Search:
    binary_Search(0, n-1, i)
'''
