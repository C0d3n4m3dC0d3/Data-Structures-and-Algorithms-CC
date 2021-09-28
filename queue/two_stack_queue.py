class Stack:
	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		if not len(self.stack) == 0:
			return self.stack.pop()
		return None

	def is_empty(self):
		return len(self.stack) == 0

	def top(self):
		if len(self.stack) == 0:
			return "Stack Undeflow"
		return self.stack[-1]

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, val):
        while len(self.s1.stack) != 0:
            self.s2.push(self.s1.stack[-1])
            self.s1.pop()

        self.s1.push(val)
        while len(self.s2.stack) != 0:
            self.s1.push(self.s2.stack[-1])
            self.s2.pop()

    def dequeue(self):
	    if len(self.s1.stack) == 0:
		    print("Q is Empty")
	    val = self.s1.stack[-1]
	    self.s1.pop()
	    return val

if __name__ == '__main__':
	queue = Queue()

	for i in range(4):
		queue.enqueue(i*i)

	for i in range(3):
		print(queue.dequeue())
