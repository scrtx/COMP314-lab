class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(bst):
        bst._size = 0
        bst._root = None
    
    def size(bst):
        return bst._size
    
    def root(bst):
        return bst._root
    
    def add(bst, key, value):
        bst._size += 1
        
        if bst.root() is None:
            bst._root = Node(key, value)
            return

        curr = bst.root()
        prev = None
        newNode = Node(key, value)
        
        while curr != None:
            prev = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        
        curr = newNode
        
        if(prev.key > curr.key):
            prev.left = curr
        else:
            prev.right = curr

    def search(bst, key):    
        curr = bst.root()
        
        while( curr != None ):
            if key == curr.key:
                return curr.value
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
    
        return False
        
    def smallest(bst):
        if bst.root() is None:
            print("BST is Empty.")
            return False
        
        curr = bst.root()
        
        while(curr.left != None):
            curr = curr.left
        else:
            return (curr.key, curr.value)    
    
    def largest(bst):
        if bst.root() is None:
            print("BST is Empty.")
            return False
        
        curr = bst.root()
        
        while(curr.right != None):
            curr = curr.right
        else:
            return (curr.key, curr.value) 
    
    def remove(bst, key):
        if not bst.search(key):
            print("Target not in BST.")
            return False
        
        bst._size -= 1
        curr = bst.root()
        while curr != None:
            if key < curr.key:
                parent = curr
                curr = curr.left
            elif key > curr.key:
                parent = curr
                curr = curr.right
            else:
                # Case 1: Node has no children
                if (curr.left is None and curr.right is None):
                    if curr == bst.root():
                        bst._root = None
                    elif curr == parent.left:
                        parent.left = None
                    else:
                        parent.right = None 
                    curr = None               
                
                # Case 2: Node has one child
                elif curr.left is None:
                    if curr == bst.root():
                        bst._root = curr.right
                    elif curr == parent.left:
                        parent.left = curr.right
                    else:
                        parent.right = curr.right
                    curr = None

                elif curr.right is None:
                    if curr == bst.root():
                        bst._root = curr.left
                    elif curr == parent.left:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left
                    curr = None
                
                # Case 3: Node has two children
                else:
                    succ = curr.right
                    succ_prev = curr

                    while succ.left is not None:
                        succ_prev = succ
                        succ = succ.left

                    curr.key = succ.key
                    curr.value = succ.value

                    if succ == succ_prev.left:
                        succ_prev.left = succ.right
                    else:
                        succ_prev.right = succ.right
                    break    
       
    def inorder_walk(bst, root):
        keys = []
        if root is not None:
            keys += bst.inorder_walk(root.left)
            keys.append(root.key)
            keys += bst.inorder_walk(root.right)
        return keys
    
    def preorder_walk(bst, root):
        keys = []
        if root is not None:
            keys.append(root.key)
            keys += bst.preorder_walk(root.left)
            keys += bst.preorder_walk(root.right)
        return keys

    def postorder_walk(bst, root):
        keys = []
        if root is not None:
            keys += bst.postorder_walk(root.left)
            keys += bst.postorder_walk(root.right)
            keys.append(root.key)
        return keys
            
    #end of class

# if __name__=='__main__':
#     bst = BinarySearchTree()
#     bst.add(10, ":)")
#     bst.add(16, ":O")
#     bst.add(5, "Hi")
#     bst.add(13, "(.Y.)")
#     bst.add(19, "Johnathan")
#     bst.add(15, ":O")
#     bst.add(8, "Thomas")
#     bst.add(4, "<O_o>")
#     bst.inorder_walk(bst.root())
#     print('\n')
#     bst.preorder_walk(bst.root())
#     print('\n')
#     bst.postorder_walk(bst.root())
#     print('\n')
#     print(bst.smallest())
#     print(bst.largest())
#     print(bst.search(13))
#     bst.remove(4)
#     bst.inorder_walk(bst.root())
#     print('\n')
#     bst.remove(13)
#     bst.inorder_walk(bst.root())
#     print('\n')
#     bst.remove(10)
#     bst.inorder_walk(bst.root())
#     print('\n')
#     bst.preorder_walk(bst.root())
#     print('\n')
#     bst.postorder_walk(bst.root())
