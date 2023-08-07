from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i] # tmp는 삽입하기 위한 값
        while j > 0 and a[j - 1] > tmp: # tmp보다 앞이 크다면
            a[j] = a[j - 1] # 뒤로 미룬다
            j -= 1
        a[j] = tmp # 적합한 자리에 tmp를 삽입한다

# 이진 삽입 정렬 (이미 정렬을 마친 배열을 제외하고 원소를 삽입할 위치를 검사)
def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1
        
        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1 # 삽입해야할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key

# 이진 삽입 정렬 - binsect.insort 사용
import bisect

def binary_insertion_insort(a: MutableSequence) -> None:
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)