#ARRAY IMPLEMENTATION
class ArrayStack:
	def __init__(self, max_size):
		self.__max_size = max_size
		self.__arr = [None]*max_size
		self.__top = -1

	def push(self, item):
		if self.__top == self.__max_size-1:
			raise Exception("Stack Overflow Exception")
		self.__top += 1
		self.__arr[self.__top] = item

	def pop(self):
		if self.__top == -1:
			raise Exception("Stack Underflow Exception")
		pop_item = self.__arr[self.__top]
		self.__top -= 1
		return pop_item

	def isEmpty(self):
		return self.__top == -1

	def top(self):
		if self.__top == -1:
			raise Exception("Stack Underflow")
		return self.__arr[self.__top]

	def peek(self, i): #i = 0 -> top, i = 1->top - 1, i = 2 -> top-2
		index = self.__top - i
		if index < 0:
			return None #indicates no element at this depth
		return self.__arr[index]

#LINKED LIST IMPLEMENTATION
class Node:
	def __init__(self, data):
		self.next = None
		self.data = data

class LinkedListStack:
	def __init__(self):
		self.__head = None

	def push(self, data):
		node = Node(data)
		node.next = self.__head
		self.__head = node

	def pop(self):
		if self.__head == None:
			raise Exception("Stack Underflow")
		ret = self.__head.data
		self.__head = self.__head.next
		return ret

	def is_empty(self):
		return self.__head == None

	def top(self):
		if self.__head == None:
			raise Exception("Stack Underflow")
		return self.__head.data

	def peek(self, i):
		if i < 0:
			return None
		temp = self.__head
		for d in range(i):
			if temp != None:
				temp = temp.next
		if temp != None:
			return temp.data
		return None

if __name__ == '__main__':
	size = int(input("Enter stack size:"))
	opt = int(input("Select stack implementation: [1 - Array | 2 - Linked List]:"))
	stack = ArrayStack(size) if opt == 1 else LinkedListStack()
	msg = '''
			__ Menu __
			 1. Push
			 2. Pop
			 3. Peek
			 4. Top
			 5. Quit'''
	print(msg)
	while True:
		c = int(input("Enter choice: "))
		if c == 1:
			n = int(input("Enter element to push: "))
			stack.push(n)
		elif c == 2:
			print(stack.pop())
		elif c == 3:
			i = int(input("Enter index: "))
			print(stack.peek(i))
		elif c == 4:
			print(stack.top())
		else:
			break
