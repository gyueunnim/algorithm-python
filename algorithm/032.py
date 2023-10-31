# 동전 개수의 최솟값 구하기 (백준 11047)
import sys
input = sys.stdin.readline

n, target = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.reverse()

count = 0
for coin in coins:
    if coin <= target:
        count = count + int(target / coin)
        target = target % coin

print(count)