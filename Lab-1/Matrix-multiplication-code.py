#To implement matrix multiplication 
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]] 
'''Rows = int(input("Give the number of rows:"))  
Columns = int(input("Give the number of columns:"))  
X = [[int(input()) for c in range (Columns)] for r in range(Rows)]  
Y=[[int(input()) for c in range (Columns)] for r in range(Rows)]''' 
# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
print("Result of matrix multiplication is:")
for r in result:
   print(r)
