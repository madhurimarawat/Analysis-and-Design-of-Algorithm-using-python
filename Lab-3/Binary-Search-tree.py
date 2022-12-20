#To implement binary search tree 
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
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
   def binarySearchtree(self, root):
      res = []
      if root:
         res = self.binarySearchtree(root.left)
         res.append(root.data)
         res = res + self.binarySearchtree(root.right)
      return res# Use the insert method to add nodes
n=int(input("Enter number of elements:"))
for i in range(0,n):
  print("Enter Element",i+1,":",end=" ")
  ele=int(input())
  if i==0:
     root = Node(ele)
  else:
     root.insert(ele)
print("Binary search tree is : ",root.binarySearchtree(root)) 