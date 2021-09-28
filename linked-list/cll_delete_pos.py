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
			return
		else:
			temp = self.head
			while True:
				print(temp.data, end=' ')
				temp = temp.next
				if temp == self.head:
					break
			print()

	def add(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
			node.next = self.head
		else:
			temp = self.head
			while True:
				if temp.next == self.head:
					break
				temp = temp.next
			node.next = temp.next
			temp.next = node
		return self

	def delete(self, pos):
		if self.head == None:
			print("Empty List!")
		else:
			if pos == 0:
				if self.head.next == self.head:
					self.head = None
				else:
					temp = self.head
					while True:
						if temp.next == self.head:
							break
						temp = temp.next
					temp.next = self.head.next
					temp = self.head
					self.head = temp.next
					temp.next = None
			else:
				count = 0
				temp = self.head
				while True and count < pos-1:
					if temp.next == self.head:
						break
					temp = temp.next
					count += 1
				if count == pos-1:
					deln = temp.next
					temp.next = deln.next
					deln.next = None
		return self

if __name__ == '__main__':
	cll = CircularLinkedList()
	cll = cll.add(0)
	cll = cll.add(1)
	cll = cll.add(2)
	cll = cll.add(3)
	cll = cll.add(4)
	cll.print_list() #0 1 2 3 4

	cll = cll.delete(0)
	cll = cll.delete(1)
	cll = cll.delete(2)
	cll.print_list() # 1 3
