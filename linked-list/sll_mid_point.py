#Find the mid point of a linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def diplay(list):
	temp = list
	while temp != None:
		print(temp.data, end=" ")
		temp = temp.next

def mid_point(list):
	p1 = list
	p2 = list
	while p2 != None:
		if p2.next == None:
			break
		p1 = p1.next
		p2 = p2.next.next
	return p1.data

if __name__ == '__main__':
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')

	a.next = b
	b.next = c
	c.next = d

	print(mid_point(a)) #case - even

	d.next = e
	print(mid_point(a)) #case - odd
