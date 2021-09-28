class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_next(bt, n):
    if bt == None:
        return "Empty Tree"
    queue = [bt]
    level = [0]
    while len(queue)>0:
        node = queue.pop(0)
        if node.data == n.data:
            if len(level) <= 1:
                return "No next node"
            if level[0] == level[1]:
                return queue[0].data
            else:
                return "No next node"

        l = level.pop(0)
        if node.left != None:
            queue.append(node.left)
            level.append(l+1)
        if node.right != None:
            queue.append(node.right)
            level.append(l+1)

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

    # find_next(root, n)
    # case 1 - when the tree is empty
    print(find_next(None, a))
        # ouput - Empty Tree

    # case 2 - when n in the root node
    print(find_next(a, a))
        # output - No Next Node
    
    # case 3 - when a valid next node exists
    print(find_next(a, b))
        # output - C
    
    # case 4 - when a valid next node does not exist
    print(find_next(a, e))
        # output - No Next Node

    # case 5 - when n is the last node in the tree     
    print(find_next(a, g))
        # output - No Next Node