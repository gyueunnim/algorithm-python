from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    maximun = a[0]
    for i in range(1, len(a)):
        if maximun < a[i]:
            maximun = a[i]

    return maximun

if __name__ == '__main__':
    num = int(input('원소수 입력: '))

    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]의 값을 입력하세요: '))

    print(f'최댓값은 {max_of(x)}')