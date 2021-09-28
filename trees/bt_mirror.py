class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bt_mirror(bt):
    if bt == None:
        return
    bt.left, bt.right = bt.right, bt.left
    bt_mirror(bt.left)
    bt_mirror(bt.right)
    return bt

def bfs(bt):
    if bt == None:
        print ("Empty Tree")
        return
    bfs_order = []
    queue = [bt]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
        bfs_order.append(node.data)
    bfs_order = ' '.join(bfs_order)
    print(bfs_order)

if __name__ == '__main__':
    a = BTNode('1')
    b = BTNode('2')
    c = BTNode('3')
    d = BTNode('4')
    e = BTNode('6')
    f = BTNode('5')
    g = BTNode('7')
    a.left = b
    a.right = c
    b.left = d
    b.right = f
    c.right = e
    f.left = g

    # case 1 - when the tree is empty
    bfs(bt_mirror(None))
    # output - Empty Tree
    print()

    # case 2 - when the tree is not empty
    bfs(a)
    bfs(bt_mirror(a))
    # output - 1 2 3 4 5 6 7
    #          1 3 2 6 5 4 7
    print()
    
    # case 3 - when the tree has only one in it
    bfs(g)
    bfs(bt_mirror(g))
    # output - 7
    #          7