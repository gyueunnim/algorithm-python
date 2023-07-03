# 1
'''
def is_odd(number) :
    if number % 2 == 1:
        return True
    else:
        return False
'''

# 2
'''
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)
'''

# 3
'''
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))
total = input1 + input2
print("두 수의 합은 %d입니다" % total)
'''

# 4
# 3번이 다르다. 사이에 띄어쓰기가 출력된다.

# 5
# f.close()를 추가해야 한다.

# 6

# 7

# 8
'''
import sys
args = sys.argv[1:]

total = 0
for i in args:
    total += int(i)

print(total)
'''