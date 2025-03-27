from linkedtree import LinkedTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest_element(root, k):
    stack = []
    current = root
    count = 0
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.val
        
        current = current.right
    return None

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)
    
    k = 3
    result = kth_smallest_element(root, k)
    def print_tree(root, level=0, prefix="Root: \n"):
        if root is not None:
            print(" " * (level * 2) + prefix + str(root.val))
            if root.left or root.right:
                if root.left:
                    print_tree(root.left, level + 1, "L--> ")
                else:
                    print(" " * ((level + 1) * 4) + "L--> None")
                if root.right:
                    print_tree(root.right, level + 1, "R--> ")
                else:
                    print(" " * ((level + 1) * 4) + "R--> None")

    print("BST structure:")
    print_tree(root)
    print(f"The {k}th smallest element is: {result}")  # Should print 4