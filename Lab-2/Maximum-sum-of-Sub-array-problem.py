def maxSubArray(nums):
      """
      :type nums: List[int]
      :rtype: int
      """
      dp = [0 for i in range(len(nums))]
      dp[0] = nums[0]
      for i in range(1,len(nums)):
         dp[i] = max(dp[i-1]+nums[i],nums[i])
      #print(dp)
      return max(dp)
arr=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
  print("Enter Element",i+1,":",end=" ")
  ele=int(input())
  arr.append(ele)
max_sum = maxSubArray(arr)
print("Maximum contiguous sum is ", max_sum)