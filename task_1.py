class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def findMax(node):
    """
    Функція, яка знаходить найбільше значення в двійковому дереві пошуку або AVL-дереві.
    """
    current = node
    while current.right is not None:
        current = current.right
    return current.val


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(30)

print("Найбільше значення в дереві:", findMax(root))