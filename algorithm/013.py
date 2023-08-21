# 카드 게임 (백준 2164)
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])
'''
# 시간 초과 발생
import sys
input = sys.stdin.readline
n = int(input())

queue = [i for i in range(1, n + 1)]
top = 0

while len(queue) != 1:
    queue.pop(0)
    queue.append(queue.pop(0))

print(*queue)
'''