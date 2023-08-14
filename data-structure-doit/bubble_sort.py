from typing import MutableSequence

# 버블 정렬
'''
def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
'''

# 버블 정렬 알고리즘 개선1 - 교환 0번 발생 시 정렬 완료 -> 반복문 탈출
'''
def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1, i, -1):
        exchng = 0
        if a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            exchng += 1
        if exchng == 0:
            break
'''

# 버블 정렬 알고리즘 개선2 - 스캔 범위 제한

def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n - 1, k, k - 1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last


# 셰이커 정렬
# 홀수 패스 -> 작은 원소 맨 앞, 짜굿 패스 가장 큰 원소 맨 뒤
def shaker_sort(a: MutableSequence) -> None:
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last


print('버블 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요: '))

x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

bubble_sort(x)

print('오름차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}] = {x[i]}')

# 버블 정렬 알고리즘 정렬 과정 출력
'''
def bubble_sort_verbose(a: MutableSequence) -> None:
    ccnt = 0 # 비교 횟수
    scnt = 0 # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        print(f'패스 {i + 1}')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else ' +' if a[j - 1] > a[j] else ' -'), end='')
                print(f'{a[n - 1]:2}') 
                ccnt += 1
                if a[j - 1] > a[j]:
                    scnt += 1
                    a[j - 1], a[j] = a[j], a[j - 1]
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')
'''