# Problem: https://www.codechef.com/problems/BSTOPS

# class that represent an individual node in a BST
class Node:
    def __init__(self, key, pos):
        self.left = None
        self.right = None
        self.val = key
        self.pos = pos

# function to insert a new node with given key
def insert(root, key, pos):
    if root is None:
        return Node(key, pos)
    else:
        if root.val < key:
            root.right = insert(root.right, key, pos*2+1)
        else:
            root.left = insert(root.left, key, pos*2)
    return root

# function to search a given key in BST
def search(root, key):
    # base case: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # key is smaller than root's key
    return search(root.left, key)

# function to find the node with minimum key value in bst
def minValueNode(root):
    current = root
    # loop down to find the left most leaf
    while current.left:
        current = current.left

    return current

# function to delete key and return new root
def deleteNode(root, key):
    # base case
    if root is None:
        return root

    # if the key to be deleted is smaller than the root's key
    # then it lies in left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)

    # if the key to be deleted is greater than the root's key
    # then it lies in right subtree
    elif key > root.val:
        root.right = deleteNode(root.right, key)

    # if key is same as root's key, then this is the node to be deleted
    else:
        # node with only one child or no child
        if root.left is None:
            tmp = root.right
            root = None
            return tmp

        elif root.right is None:
            tmp = root.left
            root = None
            return tmp

        # node with two children: get the inorder successor
        # (smallest in the right subtree)
        tmp = minValueNode(root.right)

        # copy the inorder successor's content to this node
        root.key = tmp.key

        # delete the inorder successor
        root.right = deleteNode(root.right, tmp.key)

    return root

# function to display inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# function return position of node with key value
def get_position(root, key):
    node = search(root, key)
    return node.pos

if __name__ == "__main__":
    r = None
    Q = int(input())
    for i in range(Q):
        query = input()
        strArr = query.split(' ')
        key = int(strArr[1])
        cmd = strArr[0]
        if cmd == 'i':
            r = insert(r, key, 1)
            print(get_position(r, key))
        elif cmd == 'd':
            print(get_position(r, key))
            r = deleteNode(r, key)
