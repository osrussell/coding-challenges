from typing import List

"""
Given an array nums of size n with only 2 types of elements, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

"""

class Solution:
    # using a dictionary 
    def majorityElement1(self, nums: List[int]) -> int:
        my_dict = {} # creates a dictionary for found numbers
        for x in nums:
            my_dict[x] = my_dict.get(x, 0) + 1 #sets dict to 1 if not in dictionary, adds 1 to value otherwise
        for i, v in my_dict.items():
            if v >= (len(nums)/2):
                return i
    
    # not using a dictionary
    # better memory but less fast (because of more comparisons?)
    def majorityElement2(self, nums: List[int]) -> int:
        element = nums[0] # stores one element
        max = 0 # store total number of a's
        for x in nums: 
            if x == element:
                max += 1 # increases max if current max element appears again
            else:
                max -= 1 # decreases max if other element appears
                if max == -1: # other element has appeared more
                    element = x
                    max = 1
        return element

            # these allow for earlier return if one element type is over half the length
    
sol = Solution()
print(sol.majorityElement1([1, 2, 1, 1, 2, 2, 1]))
print(sol.majorityElement2([1, 2, 1, 1, 2, 2, 1]))