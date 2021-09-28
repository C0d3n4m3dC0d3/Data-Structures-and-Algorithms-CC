class BT:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def print_tree(t, lvl):
	if t == None:
		if lvl == 0:
			print("Empty Tree")
		else:
			return
	else:
		for i in range(lvl):
			print(' ', end='')
		print(t.data)
		print_tree(t.left, lvl+1)
		print_tree(t.right, lvl+1)

def height(t):
	if t == None:
		return 0
	count = 0
	count = max(count, height(t.left))
	count = max(count, height(t.right))
	return count+1

if __name__ == '__main__':
	a = BT('A')
	b = BT('B')
	c = BT('C')
	d = BT('D')
	e = BT('E')
	f = BT('F')
	a.left = b
	b.left = c
	b.right = d
	c.left = e
	d.right = f
	print_tree(a, 0)
	print_tree(None, 0)

	print(height(None)) #0
	print(height(a)) #4
	print(height(b)) #3
	print(height(c)) #2
	print(height(f)) #1
