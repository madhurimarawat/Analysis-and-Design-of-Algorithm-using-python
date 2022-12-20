#To implement local minima in array and local minima in grid problem
# Function to find all the local minima in the given array arr[]
def findLocalMinima(n, arr):
	# Empty lists to store points of
	# local minima
	mn = []
	# Checking whether the first point is minima 
	if(arr[0] < arr[1]):
		mn.append(0)
	# Iterating over all points to check
	# local  minima
	for i in range(1, n-1):
		# Condition for local minima
		if(arr[i-1] > arr[i] < arr[i + 1]):
			mn.append(i)      
	# Checking whether the last point is
	# local minima 
	if(arr[-1] < arr[-2]):
		mn.append(n-1)
		# Print all the local  minima indexes stored
	if(len(mn) > 0):
		print("Points of Local minima"\
			" are : ", end ='')
		print(*mn)
	else:
		print("There are no points"\
			" of Local minima.")
# Driver Code
arr=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
  print("Enter Element",i+1,":",end=" ")
  ele=int(input())
  arr.append(ele)
# Function Call
findLocalMinima(n, arr)

