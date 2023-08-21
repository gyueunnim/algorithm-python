# 절댓값 힙 구현하기 (백준 11286)
from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    x = int(input())
    if x == 0:
        if myQueue.empty():
            print(0)
        else:
            temp = myQueue.get()
            print(temp[1])
    else:
        # 절댓값을 기준, 음수 우선 정렬
        # (절댓값, 원래값)순 튜플로 우선순위 큐에 enque
        myQueue.put((abs(x), x)) 