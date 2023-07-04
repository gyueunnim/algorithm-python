'''
height = int(input("당신의 키는 몇 cm인가요? "))
weight = ((height/100))**2 * 22
print("키 %dcm에 적절한 몸무게는 %.1fkg입니다." % (height, weight))
'''

'''
import winsound
import time

year = int(input("당신은 몇 년도에 태어났나요? "))
age = 2023-year+1
print("당신은 지금 %d살이군요." % (age))
winsound.Beep(500, 100)
winsound.Beep(500, 100)

if age>=20:
    print("당신은 성인이군요.")
else: # 나머지(20살 미만)
    print("당신은 미성년자군요.")

time.sleep(0.5)
print("당신은 %d년에 초등학교에 입학했겠군요" % (year+8-1))
time.sleep(0.5)
print("당신은 %d년에 중학교에 입학했겠군요" % (year+14-1))
time.sleep(0.5)
print("당신은 %d년에 고등학교에 입학했겠군요" % (year+17-1))
'''
'''
import winsound
import time

height = int(input("키 입력 cm 단위 : "))
weight = int(input("몸무게 입력 kg 단위 : "))

tmp = height-100
result = weight/tmp

print("<< 분석 결과 >>")

winsound.Beep(500, 100)
winsound.Beep(500, 100)
winsound.Beep(500, 100)
time.sleep(1)


print("건강상태", end=" : ")
if result<0.9:
    print("저체중")
elif 0.9<=result and result<=1.1:
    print("정상")
else: # 1.1 초과
    print("비만")
'''
'''
height = int(input("키 입력 (cm단위) : "))
weight = int(input("몸무게 입력 (kg) : "))
height /= 100 # meter 단위
print("당신의 BMI는 %.2f입니다." % (weight / (height**2)))
'''
'''
height = int(input("키 입력 (cm단위) : "))
weight = int(input("몸무게 입력 (kg) : "))
height /= 100 # meter 단위
bmi = weight / (height**2)
print("당신의 BMI는 %.2f입니다." % bmi)
print("당신의 BMI는", end=" ")
if bmi<20:
    print("저체중 범위 입니다.")
elif 20<=bmi and bmi<25:
    print("정상체중 범위 입니다.")
elif 25<=bmi and bmi<30:
    print("경도비만 범위 입니다.")
elif 30<=bmi and bmi<40:
    print("비만 범위 입니다.")
else: # bmi 40 이상
    print("고도비만 범위 입니다.")
'''