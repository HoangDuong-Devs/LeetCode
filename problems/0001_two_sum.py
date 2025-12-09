"""
================================================================================
LeetCode #1: Two Sum
================================================================================
Difficulty: Easy
Date Solved: 2025-07-25
Link: https://leetcode.com/problems/two-sum/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Given an array of integers `nums` and an integer `target`, return indices of 
the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

--------------------------------------------------------------------------------
Solution Approach: 
    1. Brute Force - O(n²)
    2. Hash Map - O(n)
--------------------------------------------------------------------------------
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        Brute Force Approach - O(n²)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for idx, num in enumerate(nums):
            nums_to_find = target - num
            for i in range(idx + 1, len(nums)):
                if nums[i] == nums_to_find:
                    output.append(idx)
                    output.append(i)
                    return output
        return output

    def twoSum_optimized(self, nums, target):
        """
        Hash Map Approach - O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[num] = idx
            

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3, 3], 6))           # Output: [0, 1]
    print(s.twoSum_optimized([3, 3], 6)) # Output: [0, 1]
