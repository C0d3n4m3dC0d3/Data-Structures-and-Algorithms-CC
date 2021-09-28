class ArrayQueue:
	def __init__(self, size):
		self.size = size
		self.arr = [None]*size
		self.front = -1
		self.rear = -1

	def is_empty(self):
		return self.front == -1 and self.rear == -1

	def is_full(self):
		return (self.rear + 1) % self.size == self.front

	def enqueue(self, value):
		if self.is_full():
			print("Queue is full!")
		else:
			if self.front == -1:
				self.front = 0
			self.rear = (self.rear+1)%self.size
			self.arr[self.rear] = value

	def dequeue(self):
		if self.is_empty():
			print("Queue is empty!")
		elif self.front == self.rear:
				self.front = -1
				self.rear = -1
		else:
			self.front = (self.front + 1)%self.size

	def peek(self):
		if self.is_empty():
			print("Queue is empty!")
		else:
			print(self.arr[self.front])

if __name__ == '__main__':
	queue = ArrayQueue(5)

	for i in range(5):
		queue.enqueue(i+10)

	queue.peek()
	queue.enqueue(50)
	queue.dequeue()
	queue.peek()

	for i in range(5):
		queue.dequeue()
