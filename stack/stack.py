#Stack Implementation using Array
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


#Stack Implementation using Python List
class PythonListStack:
	def __init__(self):
		self.__arr = []

	def push(self, item):
		self.__arr.append(item)

	def pop(self):
		if not len(self.__arr) == 0:
			return self.__arr.pop()
		return None

	def is_empty(self):
		return len(self.__arr) == 0

	def top(self):
		if len(self.__arr) == 0:
			return "Stack Undeflow"
		return self.__arr[-1]

	def peek(self, i):
		index = -1+i
		if index < 0:
			return None
		return self.__arr[index]


class Node:
	def __init__(self, data):
		self.next = None
		self.data = data


#Stack Implementation using Linked List
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

def main():
	'''
	#stack 1
	stack1 = ArrayStack(5)
	for i in range(5):
		stack1.push(i)
	for i in range(6):
		if not stack1.isEmpty():
			print(stack1.pop())
		else:
			print("Stack empty")

	#stack 2
	stack2 = ArrayStack(10)
	stack2.push("Anil")
	stack2.push("Geetha")
	stack2.push("Kamal")

	print(stack2.top())

	for i in range(5):
		print(stack2.peek(i))

	stack3 = PythonListStack()
	for i in range(7):
		stack3.push(i)
	for i in range(10):
		print(stack3.pop())

	stack4 = PythonListStack()
	stack4.push("Soobin")
	stack4.push("Yeonjun")
	stack4.push("Beomgyu")
	stack4.push("Taehyun")
	stack4.push("Huening Kai")

	print(stack4.top())

	for i in range(7):
		print(stack4.peek(i))'''

	stack5 = LinkedListStack()
	for i in range(7):
		stack5.push(i)
	for i in range(20):
		print(stack5.pop())
	print(stack5.top())
	print(stack5.peek(3))
	print(stack5.peek(9))


if __name__ == '__main__':
	main()
