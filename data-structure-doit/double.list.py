from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, data: Any = None, prev: Node = None, next: Node = None) -> None:
        self.data = data
        # prev가 참이면(None이 아니면) self.prev에 prev를 대입
        # prev가 거짓이면(None이면) self.prev에 self를 대입
        self.prev = prev or self
        self.next = next or self    

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = self.current = Node()   # 더미 노드를 생성 -> Node의 init 동작으로 자기 자신을 참조
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        cnt = 0
        ptr = self.head.next # self.head는 더미노드이므로
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        if self.is_empty():
            print('주목 노드는 없습니다')
        else:
            print(self.current.data)
    
    def print(self) -> None:
        ptr = self.head.next
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next
    
    def print_reverse(self) -> None:
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev
    
    def next(self) -> bool:
        if self.is_empty() or self.current.next is self.head:
            return False
        
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        if self.is_empty() or self.current.prev is self.head:
            return False
        
        self.current = self.current.prev
        return True
        
    def add(self, data: Any) -> None:
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        node.next = self.current.next
        self.current.next = node
        self.current = node
        self.no += 1
    
    def add_first(self, data: Any) -> None:
        self.current = self.head
        self.add(data)
    
    def add_last(self, data: Any) -> None:
        self.current = self.head.prev
        self.add(data)
    
    def remove_current_node(self) -> None:
        if not self.is_empty():
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:       # 주목 노드를 앞으로 밀었는데 head라면
                self.current = self.head.next   # 주목 노드를 다시 뒤로 민다

    def remove(self, p: Node) -> None:
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next
    
    def remove_first(self) -> None:
        self.current = self.head.next
        self.remove_current_node()
    
    def remove_last(self) -> None:
        self.current = self.head.prev
        self.remove_current_node()
    
    def clear(self) -> None:
        while not self.is_empty():
            self.remove_first()
        self.no = 0
    
    def __iter__(self) -> DoubleLinkedListIterator:
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        return DoubleLinkedListReverseIterator(self.head)

class DoubleLinkedListIterator:
    def __init__(self, head: Node):
        self.head = head
        self.current = head.next
    
    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

class DoubleLinkedListReverseIterator:
    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev
    
    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data


from enum import Enum
Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입', '머리노드삭제', '꼬리노드삭제', '주목노드출력', '주목노드이동', '주목노드역순이동', '주목노드삭제', '모든노드삭제', '검색', '멤버십판단', '모든노드출력', '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

lst = DoubleLinkedList()

while True:
    menu = select_Menu()

    if menu == Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요: ')))
    
    elif menu == Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요: ')))
    
    elif menu == Menu.주목노드바로뒤삽입:
        lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요: ')))

    elif menu == Menu.머리노드삭제:
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:
        lst.remove_last()

    elif menu == Menu.주목노드출력:
        lst.print_current_node()
    
    elif menu == Menu.주목노드이동:
        lst.next()

    elif menu == Menu.주목노드역순이동:
        lst.prev()
    
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
    
    elif menu == Menu.모든노드역순출력:
        lst.print_reverse()
    
    elif menu == Menu.모든노드스캔:
        for e in lst:
            print(e)
    
    elif menu == Menu.모든노드역순스캔:
        for e in reversed(lst):
            print(e)
    
    else:
        break