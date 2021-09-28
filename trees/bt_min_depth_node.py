from abc import abstractmethod


class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def min_depth(bt, v):
    if bt == None:
        return 0
    if bt.data == v.data:
        return 1
    m1 = min_depth(bt.left, v)
    m2 = min_depth(bt.right, v)

    if m1 == 0 and m2 == 0:
        return 0
    if m1 == 0:
        return 1 + m2
    elif m2 == 0:
        return 1 + m1
    else:
        return 1 + min(m1, m2)

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
    b.right = g
    c.right = e
    c.left = f
    d.left = g

    # case 1 - when the tree is empty
    print(min_depth(None, a))
        # output : 0

    # case 2 - when the node is the root
    print(min_depth(a, a))
        # output : 1

    # case 3 - when the node is an intermediate node
    print(min_depth(a, d))
        # output : 3

    # case 4 - when the node appears more than once
    print(min_depth(a, g))
        # output : 3