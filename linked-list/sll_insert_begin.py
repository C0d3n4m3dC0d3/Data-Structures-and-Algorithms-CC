class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
	    new = Node(data)
	    if self.head == None:
		    self.head = new
		    return self
	    new.next = self.head
	    self.head = new
	    return self

    def print_list(self):
        if self.head == None:
            print('Empty list')
        else:
            temp = self.head
            while temp != None:
                print(temp.data, end =" ")
                temp = temp.next

if __name__ == '__main__':
    list = List()

    for i in range(10,0,-1):
        list = list.insert_begin(i)

    list.print_list()
