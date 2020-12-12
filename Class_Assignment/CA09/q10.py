# Define a class for the tree node.
class Node:

    # Define your __init__() method.
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    # def insert(self, data):
# Compare the new value with the parent node
    def insert(self, data):
    # Compare the new value with the parent node
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data

    def insert_at(self, value, node):
        pass

    def get_height(self, root):
        pass

    def print_given_level(self, root, level):
        pass
    
    # Traversals
    def print_inorder(self): #LPR
        if self.left != None:
            self.left.print_inorder()
        print(self.data)
        if self.right != None:
            self.right.print_inorder()
    
    def print_preorder(self): #PLR
        print(self.data)
        if self.left != None:
            self.left.print_inorder()
        if self.right != None:
            self.right.print_inorder()    
 
 
    def print_postorder(self): #LRP
        if self.left != None:
            self.left.print_postorder()        
        if self.right != None:
            self.right.print_postorder()
        print(self.data)
    # Sum Root to Leaf Numbers
    def sum_root_to_leaf(self, root):
        pass

    # Symmetric Trees
    def is_tree_symmetric(self, root):
        pass
    
    # Find Largest and Second Largest

    def find_largest(self, root):
        pass

    def find_second_largest(self, root):
        pass

# Instantiating a tree with the root node with value (10)
root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)
root.insert(7)
# Our tree look like this now
#        10
#      /    \
#     None   None

# Adding the left child of the root to 34
#root.left = Node(24)

# Setting the right child of the root to 89
#root.right = Node(42)


# Our tree look like this now
#          10
#        /    \
#      24      42
#     /    \  /    \
#  None  None None None

r= ''
print(f"inorder print {root.print_inorder()}")
print(f"order print {root.print_preorder()}")
print(f"postorder print {root.print_postorder()}")