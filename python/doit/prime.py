# 1000 이하의 소수를 나열하기

counter = 0             # 나눗셈 횟수 카운트
ptr = 0                 # 이미 찾은 소수의 개수
prime = [None] * 500    # 소수를 저장하는 배열

# ver 1 : count = 78022
'''
for n in range(2, 1001):
    for i in range(2, n):
        counter += 1
        if n%i == 0:
            break
    else:
        print(n)
'''

# ver 2 : count = 14622 - 알고리즘 개선1
# 자기 자신보다 작은 소수로 나눠보기
'''
prime[ptr] = 2
ptr += 1

for n in range(3, 1001, 2): # 홀수만 대상
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n
        ptr += 1
'''

# ver 3 : count = 14622 - 알고리즘 개선2
# n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않음을 활용
# n의 제곱근을 기준으로 대칭을 이룬다

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2): # 홀수를 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')