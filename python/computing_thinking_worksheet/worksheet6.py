# 1
'''
data = list(range(10, 100, 7))
print(data)
'''

# 2
'''
import time
num = 10

while num <= 31:
    if (num%3) == 0:
        pass
    else :
        print(num)
        time.sleep(0.5)
    num += 1
'''

# 3
'''
import time

for i in range(1, 21):
    if (i % 4 == 0) or (i % 7 == 0):
        print(i, i)
    else:
        print(i)
    time.sleep(0.5)
'''

# 4
'''
import time
import winsound

print("-- 구구단 프로그램 --", end="\n\n")
n = int(input("구구단 몇 단을 출력해줄까요? "))
print("\n구구단 %d단 출력합니다." % n, end="\n\n")

for i in range(1, 10):
    winsound.Beep(500, 100) # 0.5초간 소리
    print("%d x %d = %d" % (n, i, n*i))
    time.sleep(0.5)
'''

# 5
'''
import time
for i in range(1, 31) :
    if i == 30:
        print("화이팅")
    elif i % 3 == 0:
        print("박수")
    elif i % 10 == 0:
        print("만세")
    else:
        print(i)
    time.sleep(0.5)
print("<프로그램을 종료합니다.>")
'''
