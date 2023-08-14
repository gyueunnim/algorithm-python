from typing import MutableSequence

# 피벗을 기준으로 배열을 두 그룹으로 나누기
def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n // 2]

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
'''
    print(f'피벗은 {x}입니다.')
     
    print('피벗 이하인 그룹입니다.')
    print(*a[0 : pl])

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1 : pl])
    
    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1 : n])
'''
'''
print('배열을 나눕니다.')
num = int(input('원소 수를 입력하세요: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}] : '))

partition(x)
'''

def qsort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right
    x = a[(left + right) // 2]

    # 배열 나누는 과정 출력
    # print(f'a[{left}] ~ a[{right}]: ', *a[left : right + 1])

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1
    
    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a) - 1)

print('퀵 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

quick_sort(x)

print('오름차순으로 정렬했습니다')
for i in range(num):
    print(f'x[{i}] = {x[i]}')