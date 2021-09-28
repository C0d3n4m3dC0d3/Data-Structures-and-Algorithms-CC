class Queue:
	def __init__(self):
		self.queue = []
		self.front = -1
		self.rear = -1

	def is_empty(self):
		return self.rear == self.front

	def enqueue(self, value):
		if self.capacity == self.rear:
			print("Queue is full!")
		else:
			self.queue.append(value)
			self.rear += 1

	def dequeue(self):
		if self.rear == self.front:
			print("Queue is empty!")
		else:
			self.queue.pop(0)
			self.rear -= 1

class Stack:
	def __init__(self, c):
		self.queue1 = Queue(c)
		self.queue2 = Queue(c)
		self.size = 0

	def push(self, elt):
		self.size += 1
		self.queue2.enqueue(elt)

		while not self.queue1.is_empty():
			self.queue2.enqueue(self.queue1.queue[0])
			self.queue1.dequeue()

		self.queue1, self.queue2 = self.queue2, self.queue1

	def pop(self):
		if (self.queue1.is_empty()):
			return
		self.queue1.dequeue()
		self.size -= 1

	def top(self):
		if (self.queue1.is_empty()):
			return -1
		return self.queue1.queue[0]


if __name__ == '__main__':
	stack = Stack(5)

	for i in range(1,4):
		stack.push(i*i)
	print(stack.top())

	for i in range(2):
		stack.pop()
	print(stack.top())
