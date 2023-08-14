# 규칙 1 적용: 각 열에 퀸을 1개만 배치
# 16,777,216가지 발생
'''
pos = [0] * 8

def put() -> None:
    # 각 열에 배치한 퀸의 위치를 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    for j in range(8):
        pos[i] = j
        if i == 7:
            put()
        else:
            set(i + 1)
'''

# 규칙 2 적용: 각 행에 퀸을 1개만 배치
# 40,320가지 발생
'''
pos = [0] * 8
flag = [False] * 8

def put() -> None:
    # 각 열에 배치한 퀸의 위치를 출력
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    for j in range(8):
        if not flag[j]:         # j행의 퀸을 0열 0행부터 배치하는 중
            pos[i] = j          # 퀸을 i열 j행에 배치
            if i == 7:
                put()
            else:
                flag[j] = True  # 앞으로 j행은 퀸 배치 불가
                set(i + 1)
                flag[j] = False # 새로운 경우를 위해 퀸 배치 허용 (0열 0행 -> 1행 -> 2행 등 새로운 경우)
'''

# 8퀸 문제 해결 프로그램
pos = [0] * 8               # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8        # 각 행에 퀸 배치 했는지?
flag_b = [False] * 15       # 오른쪽 대각선 퀸 배치 했는지?
flag_c = [False] * 15       # 왼쪽 대각선 퀸 배치 했는지?

'''
def put() -> None:
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()
'''

def put() -> None:
    for i in range(8):
        for j in range(8):
            print('■' if pos[i] == j else '□', end = '')
        print()
    print()

def set(i: int) -> None:
    for j in range(8):
        if (not flag_a[j]               # 행에 퀸이 배치되지 않았고
            and not flag_b[i + j]       # 오른쪽 대각선에 퀸이 배치되지 않았고
            and not flag_c[i - j + 7]):     # 왼쪽 대각선에 퀸이 배치되지 않았다면
            pos[i] = j          # 퀸을 i열 j행에 배치
            if i == 7:
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True  # 앞으로 행, 대각선 관련해서 배치 불가
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False # 새로운 경우를 위해 퀸 배치 허용 (0열 0행 -> 1행 -> 2행 등 새로운 경우)

set(0)