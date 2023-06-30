
'''
name = input("당신의 이름은 무엇인가요? ")
print("%s씨 안녕하세요." % name)
year = int(input("몇 년도에 태어났나요? "))
print("그러면 당신은 올해 %d살이겠군요." % (2023-year+1))
print("5년 후에는 %d살이 되겠군요." % (2023-year+1+5))
'''

'''
print("<<< 적정 몸무게 제안 프로그램 >>>")
weight = int(input("당신의 키(cm)를 입력하세요 : "))
print("정적몸무게 : %dkg" % ((weight-100) * 0.9))
'''

'''
import time
height = float(input("당신의 키는 몇 cm인가요? "))
print("인치 단위로 변환해서 알려줄께요.")
time.sleep(0.5)
print("당신의 키는 %.2finch입니다." % (height / 2.54))
'''

'''
import time
color = input("당신은 어떤 색을 좋아하나요? ")
animal = input("당신은 어떤 동물을 좋아하나요? ")
time.sleep(0.5)
print("그러면...")
time.sleep(0.5)
print("당신은 %s %s를 좋아하겠군요" % (color, animal))
'''

'''
import time
pi= 3.141592
diameter = int(input("원의 지름의 길이는 몇 미터입니까? "))
radius = diameter/2
print("그럼 반지름 %d미터이군요." % (radius))
print("원의 넓이를 계산합니다.")
time.sleep(1.5)
print("원의 넓이는 %.2f제곱미터입니다." % (radius * radius * pi))
'''

'''
number = int(input("당신이 좋아하는 숫자는 몇 입니까? "))
print("%d를 5번 거듭 곱하면 %d입니다." % (number, number**5))
print("%d를 10번 거듭 곱하면 %d입니다." % (number, number**10))
'''