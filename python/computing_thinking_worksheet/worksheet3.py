'''
height = 167
properWeight = (height-100)*0.9

print("현재 키 : ", height)
print("적정 몸무게 : ", properWeight, "kg")
'''

'''
fee = 4558000
nextFee = fee + (fee*0.035)
print(nextFee)

for i in range(4) :
    nextFee = nextFee + (nextFee*0.035)
    print(nextFee)

for i in range(5) :
    nextFee = nextFee + (nextFee*0.045)
    print(nextFee)

print("10년 후의 등록금 : ", nextFee)

'''

'''
apples = 1200
capacity = 36
boxes = 1200//36
print("꽉 찬 사과 상자 : ", boxes, "개")

extra = 1200%36
print("완성되지 않은 사과의 개수 : ", extra, "개")
'''

'''
money = 15000000
rate = 0.045
interest = 0

for i in range(5) :
    interest += (money*rate)

tax = 0.154
interest -= (interest * tax)

result = money + interest

print("원리금 : ", result, "원")
'''

import turtle as t

for i in range(5) :
    t.fd(200)
    t.lt(144)

'''
t.color('blue')
t.width(5)

for i in range(4) :
    t.fd(150)
    t.rt(90)

t.lt(60)
t.fd(150)

for i in range(2) :
    t.rt(120)
    t.fd(150)
'''
