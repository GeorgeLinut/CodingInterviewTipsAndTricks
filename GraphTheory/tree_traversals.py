class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
  
def print_inorder(root): 
  
    if root: 
  
        print_inorder(root.left)    

        print(root.val) 
  
        print_inorder(root.right)   
  
  
def print_postorder(root): 
  
    if root: 
  
        print_postorder(root.left)   

        print_postorder(root.right) 
  
        print(root.val), 
  
  
def print_preorder(root): 
  
    if root: 
  
        print(root.val), 
  
        print_preorder(root.left) 
  
        print_preorder(root.right) 