class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self, head):
		self.head = head

	def print_list(self):
		if self.head == None:
			print("Empty List!")
		else:
			temp = self.head
			while temp != None:
				print(temp.data, end=" ")
				temp = temp.next
			print()

	def reverse(self):
		curr = self.head
		prev = None
		while curr != None:
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		self.head = prev


if __name__ == '__main__':
	a = Node('A')
	b = Node('B')
	c = Node('C')
	d = Node('D')

	a.next = b
	b.next = c
	c.next = d

	sll = SinglyLinkedList(a)
	sll.reverse()
	sll.print_list()

	a = None
	sll = SinglyLinkedList(a)
	sll.reverse()
	sll.print_list()

	a = Node('A')
	sll = SinglyLinkedList(a)
	sll.reverse()
	sll.print_list()
