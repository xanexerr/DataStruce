class Node:
    def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __str__(self):
            return str(self.data)

class CircularLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node

    def remove_node(self, key):
        if self.head:
            current = self.head
            while True:
                if current.data == key:
                    if current.next == current:  # Only one node in the list
                        self.head = None
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        if current == self.head:  # If deleting the head, move it
                            self.head = current.next
                    return
                current = current.next
                if current == self.head:
                    break

    def traverse_forward(self):
        if not self.head:
            return []
        result = []
        current = self.head
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result

    def traverse_backward(self):
        if not self.head:
            return []
        result = []
        current = self.head.prev
        while True:
            result.append(current.data)
            current = current.prev
            if current == self.head.prev:
                break
        print(" -> ".join(map(str, result)))

    def __str__(self):
        return " -> ".join(map(str, self.traverse_forward())) if self.head else "Empty List"
