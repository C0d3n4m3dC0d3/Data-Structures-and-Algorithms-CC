#Delete a doubly linked list
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

    def add(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
            return self
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        node.prev = temp

def delete_from_dll(list, pos):
    if list.head == None:
        print('Empty list')
    else:
        temp = list.head
        if pos == 0:
            del_n = temp
            temp = temp.next
            del_n.next = None
            temp.prev = None
            list.head = temp
            return list

        count = 0
        while temp.next != None and count < pos:
            temp = temp.next
            count += 1
        if count == pos:
            if temp.next != None:
                temp.next.prev = temp.prev
            temp.prev.next = temp.next
            del_n = temp
            temp = temp.next
            del_n.next = None
            del_n.prev = None
        else:
            print(pos, 'Index out of range')
        return list

if __name__ == '__main__':
    dll = DoublyLinkedList()

    dll.add(4)
    dll.add(2)
    dll.add(3)
    dll.add(1)
    dll.add(0)

    dll.print_list() #4 2 3 1 0
    print()

    dll =delete_from_dll(dll, 0)
    dll = delete_from_dll(dll, 1)
    dll = delete_from_dll(dll, 2)
    dll.print_list() #2 1
