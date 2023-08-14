from __future__ import annotations
from typing import Any, Type
import hashlib

from enum import Enum

# 해시법 - 체인법
# 노드 (연결리스트)
class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next

# 해시 클래스
class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        # key가 int형이 아닌 경우 표준 라이브러리로 형 변환을 통해 해쉬값을 얻는다
        # sha256: RSA의 바이트 문자열의 해시값을 구하는 알고리즘
        # encode: sha256에 바이트 문자열 전달을 위해 key를 str형으로 변환한 뒤 바이트 문자열 생성
        # hexidigest: sha256에서 해시값을 16진수 문자열로 꺼냄
        # int: 16진수 문자열로 하는 int형으로 반환
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity) 
    
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key) # 검색하는 key의 해쉬값
        p = self.table[hash]        # 해당 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        
        return None
    
    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key) # 추가하는 key의 해쉬값
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash]) # temp는 self.table[hash]가 참조하는 곳을 참조
        self.table[hash] = temp                   # self.table[hash]는 temp를 참조 (노드 추가)
        return True
    
    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        
        return False
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  -> {p.key} ({p.value})', end='')
                p = p.next
            print()


Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])
def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChainedHash(13)

while True:
    menu = select_menu()

    if menu == Menu.추가:
        key = int(input('추가할 키를 입력하세요: '))
        val = input('추가할 값을 입력하세요: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다.')
    
    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다.')
    
    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')
    
    elif menu == Menu.덤프:
        hash.dump()

    else:
        break
