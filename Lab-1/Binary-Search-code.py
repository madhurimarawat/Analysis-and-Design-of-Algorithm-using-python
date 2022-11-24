def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
list1=list()
n=int(input("Enter number of elements:"))
for i in range(0,n):
  print("Enter Element",i+1,":",end=" ")
  ele=int(input())
  list1.append(ele)
key=int(input("Enter key to find:"))
result = binary_search(list1, 0, n-1, key)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
