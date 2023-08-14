from __future__ import annotations
from calendar import c
from curses.ascii import NUL
from typing import Any, Type

Null = -1

class Node:
    def __init__(self, data = Null, next = Null, dnext = Null):
        self.data = data    # 데이터
        self.next = next    # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터

class ArrayLinkedList:
    def __init__(self, capacity: int):
        self.head = Null                    # 머리 노드
        self.current = Null                 # 주목 노드
        self.max = Null                     # 사용 중인 꼬리 레코드
        self.deleted = Null                 # 프리 리스트의 머리 노드 (프리 리스트: 삭제된 레코드 그룹 관리)
        self.capacity = capacity            # 리스트의 크기
        self.n = [Node()] * self.capacity   # 리스트 본체
        self.no = 0
    
    def __len__(self) -> int:  
        return self.no
    
    def get_insert_index(self):     # 다음의 삽입할 레코드의 인덱스
        if self.deleted == Null:    # 삭제 레코드가 없을 떄
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:                   # 크기 초과
                return Null
        else:           
            rec = self.deleted               # 삽입할 위치의 인덱스를 프리 리스트의 머리 노드로 부터 가져옴
            self.deleted = self.n[rec].dnext # 프리 리스트의 머리 노드를 삽입한 노드의 다음으로 최신화
            return rec

    def delete_index(self, idx: int) -> None: # 레코드[idx]를 프리 리스트에 등록함
        if self.deleted == Null:    # 삭제 레코드가 없을 때
            self.deleted - idx
            self.n[idx].dnext = Null      # idx를 프리 리스트 맨 앞에 등록
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec # idx를 프리 리스트 맨 앞에 삽입
    
    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null
    
    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0
    
    def add_first(self, data: Any):
        ptr = self.head
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec
            self.n[self.head] = Node(data, ptr)
            self.no += 1
    
    def add_last(self, data: Any) -> None:
        if self.head == Null:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next != Null: # 마지막 노드까지 이동
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1
        
    def remove_first(self) -> None:
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1
    
    def remove_last(self) -> None:
        if self.head != Null:
            if self.n[self.head].next == Null:  # 노드가 1개라면
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null
                self.delete_index(ptr)      # 프리 리스트에 추가하는 과정
                self.current = pre
                self.no -= 1
    
    def remove(self, p: int) -> None:
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return              # p는 리스트에 존재하지 않는다

                self.n[ptr].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)
    
    def clear(self) -> None:
        while self.head != Null:
            self.remove_first()
        self.current = Null
    
    def next(self) -> bool: # 주목 노드를 한 칸 뒤로 이동
        if self.current == Null or self.n[self.current].next == Null:
            return False
        self.current = self.n[self.current].next
        return True
    
    def print_current_node(self) -> None:
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)
        
    def print(self) -> None:
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next
        
    def dump(self) -> None: # 배열을 덤프
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')
    
    def __iter__(self) -> ArrayLinkedListIterator:
        return ArrayLinkedListIterator(self.n, self.head)

class ArrayLinkedListIterator:
    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self
    
    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
        
    
from enum import Enum
Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제', '꼬리노드삭제', '주목노드출력', '주목노드이동', '주목노드삭제', '모든노드삭제', '검색', '멤버십판단', '모든노드출력', '스캔', '종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = ArrayLinkedList(100)

while True:
    menu = select_Menu()

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요: ')))
    
    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요: ')))

    elif menu == Menu.머리노드삭제:
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()

    elif menu == Menu.주목노드출력:
        lst.print_current_node()
    
    elif menu == Menu.주목노드이동:
        lst.next()
    
    elif menu == Menu.주목노드삭제:
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:
        lst.clear()

    elif menu == Menu.검색:
        pos = lst.search(int(input('검색할 값을 입력하세요: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당하는 데이터가 없습니다')
    
    elif menu == Menu.멤버십판단:
        print('그 값의 데이터는 포함되어' +(' 있습니다.' if int(input('판단할 값을 입력하세요: ')) in lst else ' 있지 않습니다.'))
    
    elif menu == Menu.모든노드출력:
        lst.print()
    
    elif menu == Menu.스캔:
        for e in lst:
            print(e)
    
    else:
        break