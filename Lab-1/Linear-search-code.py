def linear_Search(list1, n, key):   
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
list1=list()
n=int(input("Enter number of elements:"))
for i in range(0,n):
  print("Enter Element",i+1,":",end=" ")
  ele=int(input())
  list1.append(ele)
key=int(input("Enter key to find:"))
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  
