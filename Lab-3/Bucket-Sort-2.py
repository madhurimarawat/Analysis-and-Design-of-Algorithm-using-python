#Bucket sort in Python programming
def bucketSort(arr):
    # step 1. find max
    mx = max(arr)

    # step 2. count frequency and store counts in the 'count' array
    count = [0 for _ in range(mx + 1)]
    for item in arr:
        count[item] += 1

    # step 3. compute the max position of each number based on
    #         the frequency stored in the 'count' array
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # step 4. shift values in 'count' by one to the right
    for c in range(len(count)-1, 0, -1):
        count[c] = count[c-1]
    count[0] = 0

    # step 5. fill the result array
    res = [0] * len(arr)
    for item in arr:
        idx = count[item]
        res[idx] = item
        count[item] += 1

    # done!
    return res
arr=list()
n=int(input("Enter number of elements:"))
for i in range(0,n):
  print("Enter Element",i+1,":",end=" ")
  ele=int(input())
  arr.append(ele)
print("Sorted Array in Ascending Order: ",bucketSort(arr)
)

