# DNA 비밀번호 (백준 12891)
import sys
input = sys.stdin.readline
s_len, p_len = map(int, input().split())
s = list(input())
check_list = list(map(int, input().split()))
my_list = [0] * 4
start = 0
end = p_len - 1
count = 0 

# 초기 설정
def make_check_list(c):
    if c == 'A':
        my_list[0] += 1
    elif c == 'C':
        my_list[1] += 1
    elif c == 'G':
        my_list[2] += 1
    else:
        my_list[3] += 1

def check():
    a = 0
    for i in range(4):
        if my_list[i] >= check_list[i]:
            a += 1
    return a

for i in range(p_len):
    make_check_list(s[i])

if check() == 4:
    count += 1

while end != s_len - 1:
    if s[start] == 'A':
        my_list[0] -= 1
    elif s[start] == 'C':
        my_list[1] -= 1
    elif s[start] == 'G':
        my_list[2] -= 1
    else:
        my_list[3] -= 1
    start += 1
    end += 1
    make_check_list(s[end])
    if check() == 4:
        count += 1

print(count)

# 답안
'''
checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1    # 기본으로 충족하니 +1하고 시작
    
for i in range(P):
    myadd(A[i]) # 초기 설정

if checkSecret == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1
print(Result)
'''