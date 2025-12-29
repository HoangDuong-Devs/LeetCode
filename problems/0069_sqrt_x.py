"""
================================================================================
LeetCode #69: Sqrt(x)
================================================================================
Difficulty: Easy
Date Started: 2025-12-13
Link: https://leetcode.com/problems/sqrtx/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Given a non-negative integer x, return the square root of x rounded down to the 
nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down 
    to the nearest integer, 2 is returned.

--------------------------------------------------------------------------------
💡 Hints (Gợi ý):
--------------------------------------------------------------------------------
1. Tìm số nguyên m sao cho m*m <= x < (m+1)*(m+1)
2. Vì x <= 2^31-1, sqrt(x) <= 46340
3. Có thể dùng binary search để tìm nhanh

--------------------------------------------------------------------------------
🎯 Approach gợi ý: Binary search
--------------------------------------------------------------------------------
Dùng binary search trên range [0, x]:
- Mid = (left + right) // 2
- Nếu mid*mid <= x, tìm bên phải (có thể lớn hơn)
- Nếu mid*mid > x, tìm bên trái
- Kết quả là right khi left > right

⏰ Time Complexity mục tiêu: O(log x)
💾 Space Complexity mục tiêu: O(1)
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # TODO: Implement your solution here
        left = 0
        right = (2 ** 31 - 1) ** 0.5 // 1
        while(left <= right):
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 < x:
                left = mid + 1
            if mid ** 2 > x:
                right = mid - 1
        
        return right

if __name__ == "__main__":
    sol = Solution()
    # Test cases - uncomment khi đã implement
    print(sol.mySqrt(4))  # Expected: 2
    print(sol.mySqrt(8))  # Expected: 2