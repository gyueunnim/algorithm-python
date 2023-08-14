from typing import Any, Sequence
import copy


# ver2: 알고리즘 개선 - 보초 추가
# 종료 조건 검사 비용 무시
def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

# ver1
'''
def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1
'''

'''
num = int(input('원소 수: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

ky = int(input('검색값: '))

idx = seq_search(x, ky)

if idx == -1:
    print('검색값 없음')
else:
    print(f'검색값 x[{idx}]')
'''