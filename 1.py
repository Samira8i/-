class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        x = self.head
        while x is not None:
            print(x.value)
            x = x.next

    def find(self, val):
        x = self.head
        while x is not None:
            if x.value == val:
                return x
            x = x.next
        return None

    def find_all(self, val):
        x = self.head
        a = []
        while x is not None:
            if x.value == val:
                x.append(x)
            x = x.next
        return a

    def len(self):
        k = 0
        x = self.head
        while x is not None:
            k += 1
            x = x.next
        return k

    def clean(self):
        x = self.head
        while x is not None:
            h = x.next
            x.next = None
            x = h
        self.head = None #ваш код забыла сфотографировать, поэтому оставила свой с переменными

    def delete(self, val, all=False):
        if self.head is None:
            return
        if not all:
            x = self.head
            prev_node = None
            while x is not None:
                if x.value == val:
                    if prev_node is not None:
                        prev_node.next = x.next
                    else:
                      self.head = x.next
                    if x == self.tail:
                        self.tail = prev_node
                    if not all:
                        return
                else:
                    prev_node = x
                x = x.next #не поняла я немного второе условие, поэтому только первое...



    def insert(self, afterNode, newNode):
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
        else:
            afterNode.next = newNode
            newNode.next = afterNode.next
            if afterNode == self.tail:
                self.tail = newNode


linked_list = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

linked_list.add_in_tail(n1)
linked_list.add_in_tail(n2)
linked_list.add_in_tail(n3)
linked_list.add_in_tail(n4)

linked_list.print_all_nodes()

print(linked_list.find(2))
linked_list.delete(2)
linked_list.print_all_nodes()
# n5 = Node(5)
# linked_list.add_in_tail(n5)
# linked_list.insert(n5, n2)
# linked_list.print_all_nodes()