class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum(node):
    """
    Функція для обчислення суми всіх значень у двійковому дереві пошуку або в AVL-дереві.
    """
    if node is None:
        return 0
    else:
        return node.val + sum(node.left) + sum(node.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

print("Сума всіх значень в дереві:", sum(root))