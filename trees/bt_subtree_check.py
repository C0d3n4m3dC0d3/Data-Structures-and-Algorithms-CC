class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def subtree_check(bt1, bt2):
    if bt1 == None or bt2 == None:
        return 'Empty Tree(s)'
    in1 = inorder(bt1)
    in2 = inorder(bt2)
    if in2 in in1:
        return "Subtree Exists"
    else:
        return "Subtree does not Exist"

def inorder(bt):
    if bt == None:
        return''
    p = ''
    p += inorder(bt.left)
    p += bt.data
    p += inorder(bt.right)
    return p


if __name__ == '__main__':
    # constructing binary tree one
    z = BTNode('A')
    y = BTNode('B')
    x = BTNode('C')
    w = BTNode('D')
    v = BTNode('E')
    u = BTNode('F')
    t = BTNode('G')
    z.left = y
    z.right = x
    y.left = w
    y.right = v
    x.right = u
    w.left = t

    # constructing binary tree two
    b = BTNode('B')
    d = BTNode('D')
    e = BTNode('E')
    g = BTNode('G')
    h = BTNode('H')
    b.left = d
    b.right = e
    d.left = g

    # case 1 - when the both trees are empty
    print(subtree_check(None, None))
        # output - Empty Tree(s)

    # case 2 - when one of trees is empty
    print(subtree_check(None, b))
        # output - Empty Trees(s)

    # case 3 - when a subtree exists
    print(subtree_check(z, b))
        # output - Subtree Exists

    # case 4 - when a subtree does not exist
    e.right = h
    print(subtree_check(z, b))
        # output - Subtree does not Exist