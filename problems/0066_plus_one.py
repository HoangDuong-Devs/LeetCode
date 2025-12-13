"""
================================================================================
LeetCode #66: Plus One
================================================================================
Difficulty: Easy
Date Started: 2025-12-09
Link: https://leetcode.com/problems/plus-one/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Cho một mảng digits đại diện cho một số nguyên lớn, trong đó digits[i] là 
chữ số thứ i của số nguyên. Các chữ số được sắp xếp từ chữ số có nghĩa 
cao nhất đến thấp nhất (từ trái sang phải).

Nhiệm vụ: Cộng thêm 1 vào số nguyên này và trả về mảng kết quả.

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: 123 + 1 = 124

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: 4321 + 1 = 4322

Example 3:
    Input: digits = [9]
    Output: [1,0]
    Explanation: 9 + 1 = 10
    ⚠️ Edge case: Có nhớ (carry)!

Example 4 (ẩn):
    Input: digits = [9,9,9]
    Output: [1,0,0,0]
    Explanation: 999 + 1 = 1000
    ⚠️ Edge case: Tất cả đều là 9!

--------------------------------------------------------------------------------
💡 Hints (Gợi ý):
--------------------------------------------------------------------------------
1. Bắt đầu cộng từ chữ số CUỐI CÙNG (hàng đơn vị)
2. Khi nào cần "nhớ" (carry)?
3. Trường hợp đặc biệt: tất cả đều là 9 → cần thêm 1 chữ số ở đầu

--------------------------------------------------------------------------------
🎯 Approach gợi ý: Simulate phép cộng
--------------------------------------------------------------------------------
Mô phỏng cách cộng tay:
- Duyệt từ cuối mảng
- Cộng 1, nếu >= 10 thì carry, tiếp tục
- Nếu không có carry thì dừng sớm

⏰ Time Complexity mục tiêu: O(n)
💾 Space Complexity mục tiêu: O(1) hoặc O(n) nếu cần mở rộng mảng
"""

class Solution(object):
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        original_number = 0
        max_level = len(digits) - 1
        level = len(digits) - 1
        while(level >= 0):
            original_number += digits[level] * (10 ** (max_level - level))
            level -= 1

        number_plusone = original_number + 1

        results = []

        while number_plusone != 0:
            results.append(number_plusone % 10)
            number_plusone = number_plusone // 10
        
        return results[::-1]

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
            
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9 and carry == 1:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
                    
        if digits[0] == 0 :
            digits.insert(0, 1)
        
        return digits

if __name__ == "__main__":
    sol = Solution()
    
    # Test cases - uncomment khi đã implement
    print(sol.plusOne([1, 2, 3]))  # Expected: [1, 2, 4]
    print(sol.plusOne([4, 3, 2, 1]))  # Expected: [4, 3, 2, 2]
    print(sol.plusOne([9]))  # Expected: [1, 0]
    print(sol.plusOne([9, 9, 9]))  # Expected: [1, 0, 0, 0]
