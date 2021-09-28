class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def identical_check(bt1, bt2):
    if bt1 == None or bt2 == None:
        return "Empty Tree(s)"
    pre1 = preorder(bt1)
    pre2 = preorder(bt2)
    if len(pre1) != len(pre2):
        return "Not Identical"
    in1 = inorder(bt1)
    in2 = inorder(bt2)
    if pre1 == pre2 and in1 == in2:
        return "Identical"
    else:
        "Not Identical"

def preorder(bt):
    if bt == None:
        return''
    p = ''
    p += bt.data
    p += preorder(bt.left)
    p += preorder(bt.right)
    return p

def inorder(bt):
    if bt == None:
        return''
    p = ''
    p += inorder(bt.left)
    p += bt.data
    p += inorder(bt.right)
    return p


if __name__ == '__main__':
    # constructing binary_tree 1
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

    # constructing binary_tree 2
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
    y.right = u
    x.right = v
    w.left = t

    # identical check
    # case 1 - when one or both trees are empty
    print(identical_check(None, None))
        # output - Empty Tree(s)
    print(identical_check(None, z))
        # output - Empty Tree(s)
    print(identical_check(a, None))
        # output - Empty Trees(s)


    # case 2 - when both trees are identical
    print(identical_check(a, z))
        #output - Identical
    
    # case 3 - when both trees are not identical
    s = BTNode('H')
    v.left = s
    print(identical_check(a, z))
        #output - Not Identical