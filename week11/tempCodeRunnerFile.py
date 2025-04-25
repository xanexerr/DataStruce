<<<<<<< HEAD
   def print_tree(root, prefix="", is_left=True):
        if not root:
            return
        
        # Print the current node with its connections
        print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
        
        # Prepare the prefix for children
        new_prefix = prefix + ("    " if is_left else "│   ")
        
        # Print right child first (will appear above)
        if root.right:
            print_tree(root.right, new_prefix, False)
        
        # Print left child
        if root.left:
=======
   def print_tree(root, prefix="", is_left=True):
        if not root:
            return
        
        # Print the current node with its connections
        print(prefix + ("└── " if is_left else "┌── ") + str(root.val))
        
        # Prepare the prefix for children
        new_prefix = prefix + ("    " if is_left else "│   ")
        
        # Print right child first (will appear above)
        if root.right:
            print_tree(root.right, new_prefix, False)
        
        # Print left child
        if root.left:
>>>>>>> 9e27ab5b329a795e16a958d6379acd18504b93e3
            print_tree(root.left, new_prefix, True)