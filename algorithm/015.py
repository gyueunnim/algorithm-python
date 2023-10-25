# 수 정렬하기 1 (백준 2750)
n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

'''
n = int(input())
a = []

for i in range(n):
    a.append(int(input()))
'''

for i in range(n):
    print(a[i])

'''
for i in a:
    print(i)
'''