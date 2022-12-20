#To implement local minima in grid problem
import numpy as np
def minima(data):
    a = np.pad(data, (1, 1),
           mode='constant',
           constant_values=(np.amax(data), np.amax(data)))
    loc_min = []
    rows = a.shape[0]
    cols = a.shape[1]
    for ix in range(0, rows - 1):
        for iy in range(0, cols - 1):
            if a[ix, iy] < a[ix, iy + 1] and a[ix, iy] < a[ix, iy - 1] and \
                a[ix, iy] < a[ix + 1, iy] and a[ix, iy] < a[ix + 1, iy - 1] and \
                a[ix, iy] < a[ix + 1, iy + 1] and a[ix, iy] < a[ix - 1, iy] and \
                a[ix, iy] < a[ix - 1, iy - 1] and a[ix, iy] < a[ix - 1, iy + 1]:
                temp_pos = (ix-1, iy-1)
                loc_min.append(temp_pos)
    print(loc_min)
# [(0, 0), (0, 3), (2, 2), (3, 0)]
Rows = int(input("Give the number of rows:"))  
Columns = int(input("Give the number of columns:"))  
  
# Initializing the matrix  
example_matrix = []  
print("Please give the entries row-wise:")  
# For user input  
for _ in range(Rows):  # This for loop is to arrange rows  
    r = []
    for i in range(Columns):  # This for loop is to arrange columns
        print("Enter Element :",end=" ")
        r.append(int(input()))  
    example_matrix.append(r)   
# Printing the matrix given by user  
for _ in range(Rows):  
    for __ in range(Columns):  
        print(example_matrix[_][__], end=" ")  
    print()  
minima(example_matrix)
