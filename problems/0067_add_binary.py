"""
================================================================================
LeetCode #67: Add Binary
================================================================================
Difficulty: Easy
Date Started: 2025-12-12
Link: https://leetcode.com/problems/add-binary/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Given two binary strings a and b, return their sum as a binary string.

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

--------------------------------------------------------------------------------
💡 Hints (Gợi ý):
--------------------------------------------------------------------------------
1. Bắt đầu cộng từ cuối chuỗi (bit thấp nhất)
2. Xử lý carry khi cộng 1 + 1 = 10 (binary)
3. Đừng quên reverse kết quả nếu xây dựng từ cuối

--------------------------------------------------------------------------------
🎯 Approach gợi ý: Simulate binary addition
--------------------------------------------------------------------------------
Mô phỏng phép cộng nhị phân tay:
- Duyệt từ cuối chuỗi, cộng từng bit với carry
- Nếu tổng >= 2, ghi 0 và carry = 1
- Xây dựng kết quả từ cuối về đầu

⏰ Time Complexity mục tiêu: O(max(len(a), len(b)))
💾 Space Complexity mục tiêu: O(max(len(a), len(b)))
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        c = int(a) + int(b)
        carry = 0
        if c == 0:
            return "0"
        res = ""
        while(c + carry != 0):
            c += carry
            if(c % 10) >= 2:
                x = c % 2
                res += str(x)
                carry = 1
            elif (c % 10) == 1:
                res +=  "1"
                carry = 0
            else:
                res += "0"   
                carry = 0
            c //= 10
        
        return res[::-1]


if __name__ == "__main__":
    sol = Solution()
    # Test cases - uncomment khi đã implement
    print(sol.addBinary("11", "1"))  # Expected: "100"
    print(sol.addBinary("1010", "1011"))  # Expected: "10101"