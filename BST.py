class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def search(root, key):
   
    if root is None or root.val == key:
        return root
 
    
    if root.val < key:
        print(f"Checking right subtree of {root.val}...")
        return search(root.right, key)
   
    
    print(f"Checking left subtree of {root.val}...")
    return search(root.left, key)



root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)


target = 10
print(f"Searching for {target}:")
result = search(root, target)

if result:
    print(f"Found node with value: {result.val}")
else:
    print("Value not found in tree.")