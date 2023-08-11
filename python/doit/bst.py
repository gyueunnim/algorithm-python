from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def search(self, key: Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        def add_node(node: Node, key: Any, value: Any) -> None:
            # node를 루트로 하는 서브트리에 key, value 노드를 삽입
            if key == node.key:
                return False    # key가 이진 검색 트리에 이미 존재
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
        
    def remove(self, key: Any) -> bool:
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p  # 부모 설정
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
            
        if p.left is None:              # p의 왼쪽 자식이 없으면 (자식이 없거나 1개)
            if p is self.root:          # p가 루트인 경우
                self.root = p.right     # 루트는 p의 오른쪽 자식으로 교체
            elif is_left_child:
                parent.left = p.right   # p의 좌측 자식을 바꿈 -> p의 좌측은 어차피 비었으니 우측으로
            else:
                parent.right = p.right  # p의 우측 자식을 바꿈 -> p의 좌측은 어차피 비었으니 우측으로
        elif p.right is None:           # p의 오른쪽 자식이 없으면 (자식이 없거나 1개)
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:                           # p가 서브 트리를 이루고 있으면 (자식이 2개)
            parent = p
            left = p.left               # 서브 트리 안에서 가장 큰 노드를 찾아서 자리를 바꿔줘야 함
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True

    def dump(self, reverse = False) -> None:
        def print_subtree(node: Node):
            if node is not None:        # 오름차순 출력 -> 중위 순회
                print_subtree(node.left)
                print(f'{node.key}  {node.value}')
                print_subtree(node.right)

        def print_subtree_rev(node: Node): # 내림차순 출력
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node.key}  {node.value}')
                print_subtree_rev(node.left)

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key
    
    def max_key(self) -> Any:
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
    

from enum import Enum
Menu = Enum('Menu', ['삽입', '삭제', '검색', '덤프', '키의범위', '종료'])

def select_Menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()

while True:
    menu = select_Menu()

    if menu == Menu.삽입:
        key = int(input('삽입할 키를 입력하세요: '))
        val = input('삽입할 값을 입력하세요: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')
        
    elif menu == Menu.삭제:
        key = int(input('삭제할 키를 입력하세요: '))
        tree.remove(key)

    elif menu == Menu.검색:
        key = int(input('검색할 키를 입력하세요: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다')
        else:
            print('해당하는 데이터가 없습니다.')
        
    elif menu == Menu.덤프:
        tree.dump()

    elif menu == Menu.키의범위:
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최댓값은 {tree.max_key()}입니다.')

    else:
        break