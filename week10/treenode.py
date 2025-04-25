<<<<<<< HEAD
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self, level=0):
        print(" " * level * 4 + self.data)
        for child in self.children:
            child.print_tree(level + 1)
    
def build_tree():
    abraham = TreeNode("Abraham")
    isaac = TreeNode("Isaac")
    ishmael = TreeNode("Ishmael")
    abraham.add_child(isaac)
    abraham.add_child(ishmael)
    
    jacob = TreeNode("Jacob (Israel)")
    esau = TreeNode("Esau")
    isaac.add_child(jacob)
    isaac.add_child(esau)
    
    return abraham

root = build_tree()
=======
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self, level=0):
        print(" " * level * 4 + self.data)
        for child in self.children:
            child.print_tree(level + 1)
    
def build_tree():
    abraham = TreeNode("Abraham")
    isaac = TreeNode("Isaac")
    ishmael = TreeNode("Ishmael")
    abraham.add_child(isaac)
    abraham.add_child(ishmael)
    
    jacob = TreeNode("Jacob (Israel)")
    esau = TreeNode("Esau")
    isaac.add_child(jacob)
    isaac.add_child(esau)
    
    return abraham

root = build_tree()
>>>>>>> 9e27ab5b329a795e16a958d6379acd18504b93e3
root.print_tree()