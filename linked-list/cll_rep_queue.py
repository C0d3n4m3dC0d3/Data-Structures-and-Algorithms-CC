class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedListQueue:
	def __init__(self):
		self.front = None
		self.rear = None

	def is_empty(self):
		return self.front == None

	def enqueue(self, value):
		item = Node(value)
		if self.rear == None:
			self.front = item
			self.rear = item
			return
		self.rear.next = item
		self.rear = item

	def dequeue(self):
		if self.is_empty():
			print("Queue is empty!")
		else:
			temp = self.front
			self.front = temp.next

			if self.front == None:
				self.rear = None

	def peek(self):
		if self.is_empty():
			print("Queue is empty!")
		else:
			print(self.front.data)

if __name__ == '__main__':
	queue = LinkedListQueue()

	for i in range(5):
		queue.enqueue(i+10)

	queue.enqueue(15)
	queue.peek()

	for i in range(10):
		queue.dequeue()
