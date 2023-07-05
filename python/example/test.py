# 1
# print('#'.join("a:b:c:d".split(':')))

# 2
# a = {'A': 0, 'B': 80}

# 3

# 4
'''
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total = 0
for i in list(filter(lambda x : x >= 50, A)):
    total += i
print(total)
'''

# 5
'''
def fibo(n) :
    f1 = 0
    f2 = 1
    print(f1, f2, sep=", ", end=', ')
    i = 0
    while i<n-2 :
        f3 = f1 + f2
        print(f3, end=", ")
        f1 = f2
        f2 = f3
        i += 1
    print()
fibo(5)
'''

# 6
'''
data = input()
data = data.split(',')
numData = []
for i in data :
    numData.append(int(i))
print(sum(numData))
'''

# 7
'''
n = int(input("구구단을 출력할 숫자를 입력하세요(2~9) : "))
for i in range(1, 10) :
    print("%d" % (n * i), end=' ')
print()
'''

# 8, 9 파일 관련

# 10
'''
class Calculator :
    def __init__(self, array) :
        self.data = array
    def sum(self) :
        return sum(self.data)
    def avg(self) :
        return sum(self.data) / len(self.data)

cal1 = Calculator([1, 2, 3, 4, 5])
cal2 = Calculator([6, 7, 8, 9, 10])
print(cal1.sum(), cal1.avg())
print(cal2.sum(), cal2.avg())
'''