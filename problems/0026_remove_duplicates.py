"""
================================================================================
LeetCode #26: Remove Duplicates from Sorted Array
================================================================================
Difficulty: Easy
Date Solved: 2025-07-29
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Given an integer array `nums` sorted in non-decreasing order, remove the 
duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums.

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two 
                 elements of nums being 1 and 2 respectively.

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5.

--------------------------------------------------------------------------------
Solution Approach: Two Pointers (Write Pointer)
--------------------------------------------------------------------------------
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
            
        write_pos = 0  # Con trỏ ghi (write pointer)
        
        for i in range(1, len(nums)):
            if nums[i] != nums[write_pos]:
                write_pos += 1
                nums[write_pos] = nums[i]
                
        return write_pos + 1  # Trả về số lượng phần tử duy nhất

    
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 2, 3, 4]
    k = sol.removeDuplicates(nums)
    print(f"k = {k}, nums = {nums[:k]}")  # Output: k = 4, nums = [1, 2, 3, 4]
