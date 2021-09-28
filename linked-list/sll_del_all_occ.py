class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head == None:
            self.head = node
            return self
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        return self

    def print_list(self):
        if self.head == None:
            print('Empty list')
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end =" ")
                temp = temp.next

def del_all_occ(list, value):
    temp = list.head
    prev = None
    while temp != None:
        if temp.data == value:
            if prev == None: #head
                prev = temp
                temp = temp.next
                prev.next = None
                prev = None
                list.head = temp
            elif temp.next == None: #last node
                prev.next = temp.next
                temp = temp.next
            else: #somewhere in the middle
                temp = temp.next
                prev.next.next = None
                prev.next = temp
        else:
            prev = temp
            temp = temp.next

if __name__ == '__main__':
    list = List()
    node1= Node(3)
    node2= Node(1)
    node3= Node(2)
    node4= Node(3)
    node7 = Node(3)
    node5= Node(4)
    node6= Node(3)

    list = list.add(node1)
    list = list.add(node2)
    list = list.add(node3)
    list = list.add(node7)
    list = list.add(node4)
    list = list.add(node5)
    list = list.add(node6)
    list.print_list()
    print()
    del_all_occ(list, 3)
    list.print_list()
