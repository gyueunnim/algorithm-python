import math

def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

math.factorial()

# 유클리드 호제법
def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

math.gcd()

# 재귀 알고리즘의 2가지 분석 방법
# 하향식 분석, 하향식 분석
def recur(n: int) -> int:
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

# 재귀 알고리즘의 비재귀적 표현
# 꼬리 재귀 제거
def recur2(n: int) -> int:
    while n > 0:
        recur(n - 1)
        print(n)
        n = n- 2

from fixed_stack import FixedStack as Stack
# 스택 활용
def recur3(n: int) -> int:
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)
            n = n - 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break