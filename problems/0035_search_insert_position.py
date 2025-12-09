"""
================================================================================
LeetCode #35: Search Insert Position
================================================================================
Difficulty: Easy
Date Started: 2025-12-09
Link: https://leetcode.com/problems/search-insert-position/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Cho một mảng đã sắp xếp (sorted) các số nguyên phân biệt (distinct) và một 
giá trị target:
- Nếu target có trong mảng → trả về index của nó
- Nếu target không có → trả về index mà nó SẼ được chèn vào

⚠️ YÊU CẦU: O(log n) runtime complexity!

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

--------------------------------------------------------------------------------
Constraints:
--------------------------------------------------------------------------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order
- -10^4 <= target <= 10^4

--------------------------------------------------------------------------------
💡 Hints (Gợi ý):
--------------------------------------------------------------------------------
1. O(log n) nghĩa là gì? Thuật toán nào có độ phức tạp này?
2. Mảng đã SORTED → đây là điều kiện quan trọng!
3. Khi không tìm thấy target, con trỏ nào sẽ cho ta vị trí chèn?

--------------------------------------------------------------------------------
🎯 Approach gợi ý: Binary Search
--------------------------------------------------------------------------------
- Đây là bài Binary Search cơ bản nhất
- Twist nhỏ: xử lý case không tìm thấy target

⏰ Time Complexity mục tiêu: O(log n)
💾 Space Complexity mục tiêu: O(1)
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return left


if __name__ == "__main__":
    sol = Solution()
    
    # Test cases - uncomment khi đã implement
    print(sol.searchInsert([1, 3, 5, 6], 5))  # Expected: 2
    print(sol.searchInsert([1, 3, 5, 6], 2))  # Expected: 1
    print(sol.searchInsert([1, 3, 5, 6], 7))  # Expected: 4
    print(sol.searchInsert([1, 3, 5, 6], 0))  # Expected: 0
