# 구간 합 구하기 1 (백준 11659)
import sys
input = sys.stdin.readline # 라인(\n) 단위로 읽어들이기 좋다

# sys.stdin.readLine을 제외하면 에러가 나는 이유 -> 매우 큰 값을 테스트 케이스로 넣으면 그렇게 되는 듯...

m, n = map(int, input().split()) # 데이터 개수, 합 횟수
numbers = list(map(int, input().split()))
s = [0]
temp = 0

# 구간 합 구하기
for i in numbers:
    temp += i
    s.append(temp)

for i in range(n):
    i, j = map(int, input().split())
    print(s[j] - s[i - 1])

'''
초기 제출 버전
m, n = input().split() # 데이터 개수, 합 횟수
m = int(m)
n = int(n)
s = [None] * (m + 1)
a = [None] * n

numbers = list(map(int, input().split()))

for i in range(n):
    a[i] = list(map(int, input().split()))

# 구간 합 구하기
s[0] = 0
for i in range(1, m + 1):
    s[i] = s[i - 1] + numbers[i - 1]

# 합 구하기
for i in range(n):
    i, j = a[i]
    print(s[j] - s[i - 1])
'''