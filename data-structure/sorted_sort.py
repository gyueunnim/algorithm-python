# 파이썬 내장함수 sorted() 함수
# 시간복잡도? 체크

print('sorted() 함수를 사용하여 정렬합니다')
num = int(input('원소 수를 입력하세요: '))
x = [None] * num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

x = sorted(x)
print('오름차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}]: {x[i]}')

x = sorted(x, reverse=True)
print('내림차순으로 정렬했습니다.')
for i in range(num):
    print(f'x[{i}]: {x[i]}')