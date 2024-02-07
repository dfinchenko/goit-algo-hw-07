class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findMin(node):
    """
    Функція, яка знаходить найменше значення в двійковому дереві пошуку або AVL-дереві.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current.val


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(7)

print("Найменше значення в дереві:", findMin(root))