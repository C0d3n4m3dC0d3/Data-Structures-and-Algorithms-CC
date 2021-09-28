#Insert into a doubly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head == None:
            print("Empty List")
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end=' ')
                temp = temp.next

def insert(list, node, pos):
    if pos == 0:#insert at the beginning
        if list.head == None:
            list.head = node
            return list
        node.next = list.head
        list.head.prev = node
        list.head = node
        return list
        
    #insert somewhere in btw / at the end
    else:
        count = 0
        temp = list.head
        while temp.next != None and count != pos-1:
            temp = temp.next
            count += 1
        if count == pos-1:
            node.prev = temp
            node.next = temp.next
            temp.next = node
            if node.next != None:
                node.next.prev = node
        else: #if position greater than range
            print("Position out of range")
        return list
     
if __name__ == '__main__':
    dll = DoublyLinkedList()
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')

    dll = insert(dll, n2, 0)
    dll = insert(dll, n1, 0)
    dll = insert(dll, n3, 2)
    dll = insert(dll, n4, 3)
    dll = insert(dll, n5, 5)

    dll.print_list()    