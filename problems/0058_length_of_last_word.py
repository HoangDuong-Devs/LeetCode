"""
================================================================================
LeetCode #58: Length of Last Word
================================================================================
Difficulty: Easy
Date Started: 2025-12-09
Link: https://leetcode.com/problems/length-of-last-word/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Cho một chuỗi s gồm các từ và khoảng trắng, trả về độ dài của từ CUỐI CÙNG 
trong chuỗi.

Một "từ" là chuỗi con dài nhất chỉ chứa các ký tự không phải khoảng trắng.

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: s = "Hello World"
    Output: 5
    Explanation: Từ cuối là "World" có độ dài 5

Example 2:
    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: Từ cuối là "moon" có độ dài 4
    ⚠️ Lưu ý: Có trailing spaces ở cuối!

Example 3:
    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: Từ cuối là "joyboy" có độ dài 6

--------------------------------------------------------------------------------
Constraints:
--------------------------------------------------------------------------------
- 1 <= s.length <= 10^4
- s chỉ chứa chữ cái tiếng Anh và khoảng trắng ' '
- Luôn có ít nhất một từ trong s

--------------------------------------------------------------------------------
💡 Hints (Gợi ý):
--------------------------------------------------------------------------------
1. Trailing spaces có thể gây rắc rối - xử lý chúng trước!
2. Python có built-in method nào giúp xử lý spaces không?
3. Có thể duyệt từ cuối chuỗi ngược lên - khi nào thì dừng?

--------------------------------------------------------------------------------
🎯 Approach gợi ý: String Manipulation
--------------------------------------------------------------------------------
Có nhiều cách tiếp cận:
- Cách 1: Dùng split() và lấy phần tử cuối
- Cách 2: strip() trailing spaces rồi tìm từ cuối
- Cách 3: Duyệt ngược từ cuối chuỗi

⏰ Time Complexity mục tiêu: O(n)
💾 Space Complexity mục tiêu: O(1) hoặc O(n) tùy approach
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        words = s.split()
        return len(words[-1])
        
    def lengthOfLastWord2(self, s):
        pos = len(s) - 1
        while(pos >= 0 and s[pos] == ' '):
            pos -= 1
        
        length = 0
        while(pos>=0 and s[pos] != ' '):
            pos -= 1
            length += 1
        return length



if __name__ == "__main__":
    sol = Solution()
    
    # Test cases - uncomment khi đã implement
    # print(sol.lengthOfLastWord("Hello World"))  # Expected: 5
    # print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Expected: 4
    # print(sol.lengthOfLastWord("luffy is still joyboy"))  # Expected: 6
