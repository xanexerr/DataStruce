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

    def __str__(self):
        return super().__str__()