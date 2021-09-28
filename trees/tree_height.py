class TreeNode:
	def __init__(self, data):
		self.data = data
		self.children = []

	def add_child(self, child):
		self.children.append(child)

	def print(self, level):
		for i in range(level):
			print(' ', end='')
		print(self.data)
		for child in self.children:
			child.print(level+1)


def height(t):
	if t == None:
		return 0
	count = 0  #max height of child
	for child in t.children:
		count = max(count, height(child))
	return 1 + count

if __name__ == '__main__':
	a = TreeNode('A')
	b = TreeNode('B')
	c = TreeNode('C')
	d = TreeNode('D')
	e = TreeNode('E')
	f = TreeNode('F')
	g = TreeNode('G')

	a.add_child(b)
	a.add_child(c)
	a.add_child(d)
	c.add_child(e)
	d.add_child(f)
	d.add_child(g)

	print(height(None))
	print(height(a))
	print(height(c))
	print(height(b))
