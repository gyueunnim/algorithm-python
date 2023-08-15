# 투 포인터 (백준 2018)
n = int(input())
count = 1
start = 1
end = 1
sum = start

while end != n:
    if sum == n:
        count += 1
        end += 1
        sum += end
    elif sum < n:
        end += 1
        sum += end
    else:
        sum -= start
        start += 1

        

print(count)

# 답안
'''
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end += 1
        sum += 1
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index
'''