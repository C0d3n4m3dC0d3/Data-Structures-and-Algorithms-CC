class Stack:
	def __init__(self):
		self.arr = []

	def push(self, item):
		self.arr.append(item)

	def pop(self):
		if not len(self.arr) == 0:
			return self.arr.pop()
		return None

	def is_empty(self):
		return len(self.arr) == 0

	def top(self):
		if len(self.arr) == 0:
			return "Stack Undeflow"
		return self.arr[-1]

	def peek(self, i):
		index = -1+i
		if index < 0:
			return None
		return self.arr[index]

def find_next_greatest(list):
	l = len(list)
	stack = Stack()

	stack.push(list[0])
	for i in range(1,l):
		next_elt = list[i]
		if not stack.is_empty():
			elt = stack.pop()
			while elt < next_elt:
				print(elt," - ",next_elt)
				if stack.is_empty():
					break
				elt = stack.pop()
			if elt > next_elt:
				stack.push(elt)
		stack.push(next_elt)

	while not stack.is_empty():
		elt = stack.pop()
		next_elt = -1
		print(elt, " - ", next_elt)

if __name__ == '__main__':
	list = [int(i) for i in input().split()]
	find_next_greatest(list)
