# 평균 구하기 (백준 1546)

n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum * 100 / mymax / int(n))