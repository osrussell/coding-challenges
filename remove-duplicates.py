from typing import List

"""
Level: Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Return elements left after placing the final result in the first k slots of nums.

Example:
Input: [0, 0, 1, 1, 1, 2]
Output: [0, 1, 2, _, _, _]

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 # keeps track of unique elements
        # make sure to check end case
        end = len(nums) - 1
        # base cases 
        if end == -1:
            return 0
        if end == 0:
            return 1
        for i in range(end):
            if nums[i] != nums[i+1]: # case if there is not another duplicate
                nums[k] = nums[i]
                k += 1
        if (nums[end] != nums[k-1]):
            nums[k] = nums[end]
        return k+1; # adds one to count first unique element 

sol = Solution()
print(sol.removeDuplicates([1, 1, 2, 2]))