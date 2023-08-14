# 숫자의 합 구하기 (백준 11720)

n = int(input())
numbers = list(input())
sum = 0

for i in numbers:
    sum += int(i)

print(sum)