<<<<<<< HEAD
from tree import Tree

class LinkedTree(Tree):
    # เอา LindList มาใช้เป็นโครงสร้างข้อมูล
    class Node:
        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

        def element(self):
            return self._element

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root

    def parent(self, p):
        return p._parent

    def num_children(self, p):
        return len(p._children)

    def children(self, p):
        return iter(p._children)

    def __len__(self):
        return self._size

    def add_child(self, parent, element):
        new_node = self.Node(element, parent)
        if parent is None:
            self._root = new_node
        else:
            parent._children.append(new_node)
        self._size += 1
        return new_node

    def display_hierarchy(self, p, level=0):
        print(" " * level * 4 + p.element())
        for child in self.children(p):
            self.display_hierarchy(child, level + 1)

    def find_employee_by_name(self, p, name):
        if p.element() == name:
            return p
        for child in self.children(p):
            found = self.find_employee_by_name(child, name)
            if found:
                return found
        return None

#tree traversal  มีอะไรบ้าง preorder, inorder, postorder, level order
# preorder: root -> left -> right
# inorder: left -> root -> right
# postorder: left -> right -> root
# level order: level by level from top to bottom

# เรียน tree เพื่อทำการจัดเก็บข้อมูลในรูปแบบ tree structure
# เพื่อจัดการปัญหาเรื่องการค้นหาและการจัดเก็บข้อมูลที่มีความสัมพันธ์กัน
# ปัญหาใน Runtime Complexity
=======
from tree import Tree

class LinkedTree(Tree):

    class Node:
        def __init__(self, element, parent=None):
            self._element = element
            self._parent = parent
            self._children = []

        def element(self):
            return self._element

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root

    def parent(self, p):
        return p._parent

    def num_children(self, p):
        return len(p._children)

    def children(self, p):
        return iter(p._children)

    def __len__(self):
        return self._size

    def add_child(self, parent, element):
        new_node = self.Node(element, parent)
        if parent is None:
            self._root = new_node
        else:
            parent._children.append(new_node)
        self._size += 1
        return new_node

    def display_hierarchy(self, p, level=0):
        print(" " * level * 4 + p.element())
        for child in self.children(p):
            self.display_hierarchy(child, level + 1)

    def find_employee_by_name(self, p, name):
        if p.element() == name:
            return p
        for child in self.children(p):
            found = self.find_employee_by_name(child, name)
            if found:
                return found
        return None
>>>>>>> 9e27ab5b329a795e16a958d6379acd18504b93e3
