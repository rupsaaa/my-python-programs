class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
class BTree:
    def __init__(self,root_key):
        self.root=Node(root_key)
    def insert_left(self,current_node,key):
        current_node.left=Node(key)
        return current_node.left
    def insert_right(self,current_node,key):
        current_node.right=Node(key)
        return current_node.right
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.key,end=' ')
            self.inorder(node.right)
    def preorder(self,node):
        if node:
            print(node.key,end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key,end=' ')
tree=BTree(9)
left=tree.insert_left(tree.root,7)
right=tree.insert_right(tree.root,14)
tree.insert_left(left,3)
tree.insert_right(left,8)
print("Inorder traversal of the binary tree:")
tree.inorder(tree.root)