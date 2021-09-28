class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def BFS(bt):
    if bt == None:
        print("Empty Tree")
        return
    queue = []
    queue.append(bt)
    while len(queue)>0:
        node = queue.pop(0)
        print(node.data, end='')
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    print()
if __name__ == '__main__':
    # constructing binary tree
    a = BTNode('A')
    b = BTNode('B')
    c = BTNode('C')
    d = BTNode('D')
    e = BTNode('E')
    f = BTNode('F')
    g = BTNode('G')
    a.left = b
    a.right = c
    b.left = d
    b.right = f
    c.right = e
    d.left = g


    # case 1 - Empty Binary Tree
    BFS(None)
    # output - Empty Tree
    
    # case 2 - BFS from root node
    BFS(a)
    # output - ABCDFEG

    # case 3 - BFS from intermediate node
    BFS(b)
    # output - BDFG

    # BFS from leaf node
    BFS(g)
    # output - G