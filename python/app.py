# -*- coding: utf-8 -*-

# list
usedCar1 = ['K5', 'white', 5000] 

# dictionary
usedCar2 = {
    'brand': 'BMW', 
    'model': '520d'
}

# 중고차 판매 예시

# carStock = ['K5', 'BMW', 'Tico']

# 파이썬 조건문 작성법
# if 조건식 : 
    # 조건식이 참일 때 실행할 코드

# if 'K6' in carStock :
    # print('지금 주문 가능합니다.')
# elif 'K5' in carStock :
    # print('한 대 남았습니다.')
# else :
    # print('주문 불가능')

# 파이썬 반복문 작성법
# for i in range(0, 10) :
    # print('BMW  있어요')

# usedCars = ['K5', 'BMW', 'Tico']

# for i in usedCars :
    # print(i * 3)

# for i in range(0, 3) :
    # print(usedCars[i])

# python 함수 작성법
def Hello() :
    for i in range(0, 3) :
        print('안녕하세요 중고차 판매자입니다.')
    

def Para(p) :
    print(p + 1) # 자료 변환기도 활용

def func() :
    return 10

print(func())