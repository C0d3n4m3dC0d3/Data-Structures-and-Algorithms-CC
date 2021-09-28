class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LCA(bt, n, m):
    if bt == None:
        return None
    if bt.data == n.data or bt.data == m.data:
        return bt
    left_sub = LCA(bt.left, n, m)
    right_sub = LCA(bt.right, n, m)
    if left_sub != None and right_sub != None:
        return bt
    if left_sub != None:
        return left_sub
    if right_sub != None:
        return right_sub

def print_lca(node):
    if node == None:
        print("Empty Tree")
    else:
        print(node.data)

if __name__ == '__main__':
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

    # case 1 - when the tree is empty
    print_lca(LCA(None, a, b))
    # output - Empty Tree

    # case 2 - lca of root node
    print_lca(LCA(a, a, a))
    # output - A

    #case 3 - when the lca is the root node
    print_lca(LCA(a, g, e))
    # output - A

    # case 4 - when the lca in not the root node
    print_lca(LCA(a, d, f))
    # output - B

    # case 5 - lca of parent node and child node
    print_lca(LCA(a, c, e))
    # output - C