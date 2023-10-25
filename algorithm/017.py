# 내림차순으로 자릿수 정렬하기 (백준 1427)
import sys
print = sys.stdout.write

a = list(input())

for i in range(len(a)):
    max = i

    for j in range(i+1, len(a)):
        if a[j] > a[max]:
            max = j

    if a[max] > a[i]:    
        a[i], a[max] = a[max], a[i]
        
for i in range(len(a)):
    print(a[i])