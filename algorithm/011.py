# 스택으로 수열 만들기 (백준 1874)

n = int(input())
a = [0] * n

for i in range(n):
    a[i] = int(input())

num = 1
stack = []
answer = ""
result = True

for i in range(n):
    temp = a[i]
    if temp >= num:
        while temp >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        n = stack.pop()
        if n > temp:
            print("NO")
            result = False
            break
        else:
            answer += '-\n'

if result:
    print(answer)