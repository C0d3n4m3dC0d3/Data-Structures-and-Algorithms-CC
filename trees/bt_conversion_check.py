class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def check_conversion(tree1, tree2):
    if tree1 == None or tree2 == None:
        return "Cannot be converted : Empty Tree"
    if tree1 == tree2:
        return True
    non_empty = (tree1 and tree2) and (tree1.data == tree2.data)
    same_side_equality = (check_conversion(tree1.left, tree2.left) and check_conversion(tree1.right, tree2.right))
    opp_side_equality = (check_conversion(tree1.right, tree2.left) and check_conversion(tree1.left, tree2.right))
    if non_empty and (same_side_equality or opp_side_equality):
            return "Can be converted"
    else:
        return "Cannot be converted"
if __name__ == '__main__':
    a = BTNode(1)
    b = BTNode(2)
    c = BTNode(3)
    d = BTNode(4)
    e = BTNode(5)

    a.left = b
    a.right = c
    b.left = d
    b.right =  e
    
    i = BTNode(1)
    j = BTNode(2)
    k = BTNode(3)
    l = BTNode(4)
    m = BTNode(5)

    i.left = k
    i.right = j
    k.left = l
    k.right = m

    # case 1 - when the tree is empty
    print(check_conversion(a, None))
        # output - Cannot be converted : Empty Tree
    print(check_conversion(None, None))
        # output - Cannot be converted : Empty Tree

    # case 2 - when the tree can be convereted
    print(check_conversion(a, i))
        # output - Can be converted



    i = BTNode(2)
    j = BTNode(4)
    k = BTNode(6)
    l = BTNode(8)
    m = BTNode(10)
    i.left = k
    i.right = j
    k.left = l
    k.right = m
    # case 3 - when the tree cannot be converted
    print(check_conversion(a, i))
        # output - Cannot be converted