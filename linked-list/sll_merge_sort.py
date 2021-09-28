class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			while temp.next != None:
				temp = temp.next
			temp.next = node

	def merge(self, l, r):
		res_node = None

		if l == None:
			return r
		if r == None:
			return l

		if l.data <= r.data:
			res_node = l
			res_node.next = self.merge(l.next, r)
		else:
			res_node = r
			res_node.next = self.merge(l, r.next)

		return res_node


	def merge_sort(self, head):
		if head == None or head.next == None:
			return head

		m = self.calc_mid(head)
		m_next = m.next

		m.next = None

		left = self.merge_sort(head)
		right = self.merge_sort(m_next)

		sorted_list_node = self.merge(left, right)
		return sorted_list_node

	def calc_mid(self, head):
		if head == None:
			return head

		ptr1 = head
		ptr2 = head

		while (ptr2.next != None) and (ptr2.next.next != None):
			ptr1 = ptr1.next
			ptr2 = ptr2.next.next

		return ptr1


	def print_list(self):
		if self.head == None:
			print("Empty List!")
		else:
			temp = self.head
			while temp != None:
				print(temp.data, end=" ")
				temp = temp.next
		print()

if __name__ == '__main__':
	list = LinkedList()

	list.add(20)
	list.add(60)
	list.add(10)
	list.add(15)
	list.add(5)
	list.add(25)
	list.add(30)

	list.print_list() #20 60 10 15 5 25 30
	list.head = list.merge_sort(list.head)
	list.print_list() #5 10 15 20 25 30 60
