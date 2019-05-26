class Node:
    def __init__(self, data, position):
        self.data = data
        self.position = position
        self.left = None
        self.right = None

    def insert(root, data, position):
        if root is None:
            print(position)
            return Node(data, position)
        if data < root.data:
            root.left = insert(root.left, data, 2 * position)
        else:
            root.right = insert(root.right, data, 2 * position + 1)
        return root

    def minimmum(root):
        curr = root
        while curr.left != None:
            curr = curr.left
        return curr

    def delete(root, data):
        if data < root.data:
            root.left = delete(root.left, data)
        elif data > root.data:
            root.right = delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = minimum(root.right)
            root.data = temp.data
            root.right = delete(root.right,temp.data)
        return root
        
