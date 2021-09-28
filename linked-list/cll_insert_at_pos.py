class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		if self.head == None:
			print("Empty List!")
		else:
			temp = self.head
			while True:
				print(temp.data, end=' ')
				temp = temp.next
				if temp == self.head:
					break
			print()

	# insert at position
	def insert(self, data, pos):
		node = Node(data)
		if self.head != None:
			#at the beginning
			if pos == 0:
				temp = self.head
				while True:
					if temp.next == self.head:
						break
					temp = temp.next
				node.next = temp.next
				temp.next = node
				self.head = node
			#at the end or in between
			else:
				count = 0
				temp = self.head
				while temp.next != self.head and count < pos-1:
					temp = temp.next
					count += 1
				if count == pos-1 and temp:
					node.next = temp.next
					temp.next = node
				else:
					print("Index out of range!")
		else:
			#head is None and pos == 0
			if pos == 0:
				self.head = node
				node.next = self.head
			else:
				print("Empty List!")
		return self

if __name__ == '__main__':
	cll = CircularLinkedList()
	cll = cll.insert(1, 0)
	cll = cll.insert(0, 0)
	cll = cll.insert(1, 1)
	cll = cll.insert(2, 3)
	cll = cll.insert(3, 4)
	cll.print_list() #0 1 1 2 3
