from selectors import EpollSelector
from typing import List

"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""

class Solution:
    # first attempt at a solution with a dictionary
    def singleNumber1(self, nums: List[int]) -> int:
        my_dict = {} # creates a dictionary for found numbers
        for x in nums:
            my_dict[x] = my_dict.get(x, 0) + 1 #sets dict to 1 if not in dictionary, adds 1 to value otherwise
        for i, v in my_dict.items():
            if v == 1:
                return i

    # second attempt with XOR
    def singleNumber2(self, nums: List[int]) -> int:
        xor = 0
        for x in nums:
            xor ^ x # bitwise XOR which "subtracts"
        return xor

sol = Solution()
print(sol.singleNumber1([1, 2, 1, 1, 2, 3]))