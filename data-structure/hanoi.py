# no: 원반 수, x: 시작 기둥, y: 도착 기둥
# 기둥은 1, 2, 3으로 구현
# 즉 x, y, 6 - x - y와 같음
def move(no: int, x: int, y: int) -> None: 
        # 가장 큰 원반과 나머지 원반으로 나눠서 생각
        # 나머지 원반을 옮긴다.
        if no > 1:
            move(no - 1, x, 6 - x - y)      # 나머지 원반 이동
        
        print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')

        if no > 1:
              move(no - 1, 6 - x - y, y)    # 나머지 원반을 원래 목적지로 이동
                                            # 내부적으로 재귀를 통해 가장 큰 원반과 나머지 원반을 또 나눈다

print('하노이의 탑을 구현합니다.')        
n = int(input('원반의 개수를 입력하세요: '))

move(n, 1, 3)