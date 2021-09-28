class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def symmetry_check(bt):
    if bt == None:
        return "Empty Tree"

    if mirror_check(bt.left, bt.right):
        return "Symmetric"
    return "Not Symmetric"

def mirror_check(btl, btr):
    if btl == None and btr == None:
        return True
    if btl != None and btr != None:
        if btl.data == btr.data:
            return (mirror_check(btl.left, btr.right)) and (mirror_check(btl.right,btr.left))
        return False
    return False

if __name__ == '__main__':
    a = BTNode('A')
    b1 = BTNode('B')
    c1 = BTNode('C')
    d1 = BTNode('D')
    b2 = BTNode('B')
    c2 = BTNode('C')
    d2 = BTNode('D')
    a.left = b1
    a.right = b2
    b1.left = c1
    b2.right = c2
    b1.right = d1
    b2.left = d2

    # case 1 - when the tree is empty
    print(symmetry_check(None))
        # output - Empty Tree
   
    # case 2 - when the tree is symmetric
    print(symmetry_check(a))
        # output - Symmetric

    # case 3 - when the tree has only one node
    print(symmetry_check(d2)) 
        # output - Symmetric

    # case 4 - when the tree is not symmetric
    print(symmetry_check(b2))
        # output - Not Symmetric