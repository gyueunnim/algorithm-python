# 주몽의 명령 (백준 1940)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

start = 0
end = n - 1
count = 0

while start < end:
    if numbers[start] + numbers[end] == m:
        count += 1
        end -= 1
    elif numbers[start] + numbers[end] > m:
        end -= 1
        
    else:
        start += 1

print(count)