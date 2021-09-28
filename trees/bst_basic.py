class BST:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None

#returns new tree
def rec_insert(tree, key, value):
	if tree == None:
		node = BST(key, value)
		return node
	if key <= tree.key:
		tree.left = rec_insert(tree.left, key, value)
		return tree
	else:
		tree.right = rec_insert(tree.right, key, value)
		return tree

#non-recursive insert
def insert(tree, key, value):
	if tree == None:
		return BST(key, value)
	node = tree
	parent = None
	while node != None:
		if key <= node.key:
			parent = node
			node = node.left
		else:
			parent = node
			node = node.right
	if key <= parent.key:
		parent.left = node
	else:
		parent.right = node
	return tree

#searching for node in a bst
def search(tree, key): #returns node containing the key
	if tree == None:
		return None
	node = tree
	while node != None:
		if node.key == key:
			return node
		if key < node.key:
			node = node.left
		else:
			node = node.right
	return None

#printing the tree
def print_tree(tree, level):
	if tree == None and level == 0:
		print('Empty Tree')
		return
	if tree == None:
		return
	for i in range(level):
		print(' ', end='')
	print(tree.key, tree.value)

	for i in range(level):
		print(' ', end='')
	print('Left')
	print_tree(tree.left, level+1)

	for i in range(level):
		print(' ', end='')
	print('Right')
	print_tree(tree.right, level+1)


if __name__ == '__main__':
	tree = None
	#recursive insert
	tree = rec_insert(tree, 5, 1)
	tree = rec_insert(tree, 3, 1)
	tree = rec_insert(tree, 7, 1)
	tree = rec_insert(tree, 2, 1)
	tree = rec_insert(tree, 3, 2)
	tree = rec_insert(tree, 8, 1)

	print_tree(tree, 0)

	tree1 = None
	#non-recursive insert
	tree = insert(tree, 5, 1)
	tree = insert(tree, 3, 1)
	tree = insert(tree, 7, 1)
	tree = insert(tree, 2, 1)
	tree = insert(tree, 3, 2)
	tree = insert(tree, 8, 1)

	print_tree(tree, 0)

	#search for a Node
	node = search(tree, 6)
	print(node)
	node = search(tree, 3)
	print(node.key, node.value)
