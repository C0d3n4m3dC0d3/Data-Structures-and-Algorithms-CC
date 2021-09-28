class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def height(bt):
    if bt == None:
        return 0
    return 1 + max(height(bt.left), height(bt.right))

def diameter(bt):
    if bt == None:
        return 0

    # calculating height of left side
    left_height = height(bt.left)
    right_height = height(bt.right)
    d1 = left_height + right_height + 1
    
    # calculating height of right side
    left_diameter = diameter(bt.left)
    right_diameter = diameter(bt.right)
    d2 = max(left_diameter, right_diameter)

    return max(d1, d2)

if __name__ == '__main__':
 
    a = BTNode('A')
    b = BTNode('B')
    c = BTNode('C')
    d = BTNode('D')
    e = BTNode('E')
    f = BTNode('F')
    g = BTNode('G')
    h = BTNode('H')
    i = BTNode('I')
    j = BTNode('J')
    k = BTNode('K')
    l = BTNode('L')
    a.left = b
    a.right = c
    b.left = d
    b.right = g
    d.left = e
    d.right = f
    g.right = h
    h.left = i
    h.right = j
    j.right = k
    k.left = l

    # case 1 - when the tree is empty
    print(diameter(None))
        # output - 0
    
    # case 2 - diameter of root node
    print(diameter(a))
        # output - 8
    
    # case 2 - diameter from an intermediate node
    print(diameter(d))
        # output - 3
    
    # case 3 - diameter from a leaf node
    print(diameter(c))
        # output - 1