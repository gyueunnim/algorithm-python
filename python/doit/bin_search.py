from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a)-1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        elif a[pc] > key:
            pr = pc - 1
        if pl > pr:
            break
    return -1

# 실행 과정 출력 
'''
def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a)-1

    print('   |' , end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2
        
        print('   |', end='')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n   |')

        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        elif a[pc] > key:
            pr = pc - 1
        if pl > pr:
            break
    return -1
'''
