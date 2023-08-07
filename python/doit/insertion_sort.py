from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n): # 두번째 원소부터
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp: # 삽입할 자리를 찾음
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
