#find the meeting point of a linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def meet_brute_force(l1, l2):
	p1 = l1
	while p1 != None:
		p2 = l2
		while p2 != None:
			if p1 == p2:
				return p1
			p2 = p2.next
		p1 = p1.next
	return None

def meet_point(l1, l2):
	if l1 == None or l2 == None:
		return
	p1 = l1
	p2 = l2
	while p1.next != None:
		if p1 == p2:
			return p1
		p1 = p1.next
	return None


a = Node('1')
b = Node('2')
c = Node('3')
d = Node('4')

p = Node('A')
q = Node('B')
r = Node('C')

a.next = b
b.next = c
c.next = d

p.next = q
q.next = r
r.next = c

print(meet_point(a, p))
