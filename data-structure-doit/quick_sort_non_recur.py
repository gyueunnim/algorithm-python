from fixed_stack import FixedStack as Stack
from typing import MutableSequence

# 스택을 활용해 비재귀적인 퀵 정렬 구현하기
def qsort(a: MutableSequence, left: int, right: int) -> None:
    range = Stack(right - left + 1)

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()
        x = [a(left, right) // 2]

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        
        if left < pr: range.push((left, pr))
        if pl < right: range.push(pl, right)
