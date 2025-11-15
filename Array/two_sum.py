class Solution:

    def twoSum(self, nums, target):

                
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+ nums[j]==target:
                    return i,j

numbers = [1,2,3,4,5]

target = 5

two_sum_inp = Solution()

print(two_sum_inp.twoSum(numbers,target))