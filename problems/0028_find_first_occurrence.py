"""
================================================================================
LeetCode #28: Find the Index of the First Occurrence in a String
================================================================================
Difficulty: Easy
Date Solved: 2025-12-08
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Given two strings `needle` and `haystack`, return the index of the first 
occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
                 The first occurrence is at index 0, so we return 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.

--------------------------------------------------------------------------------
Solution Approach: Sliding Window / Brute Force with Backtracking
--------------------------------------------------------------------------------
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
            
        pos = 0
        matched = 0

        while pos <= len(haystack) - len(needle):
            for char in needle:
                if char == haystack[pos + matched]:
                    matched += 1
                    if matched == len(needle):
                        return pos
                else: 
                    matched = 0
                    break
            pos += 1
        
        return -1


    # =========================================================================
    # APPROACH 2: KMP Algorithm - O(n + m) time, O(m) space
    # =========================================================================
    def strStr_KMP(self, haystack, needle):
        """
        KMP (Knuth-Morris-Pratt) Algorithm
        
        🎯 Ý tưởng chính:
        - Khi mismatch xảy ra, đừng reset về đầu!
        - Dùng thông tin đã match để "nhảy" thông minh
        - Xây bảng LPS để biết nhảy bao xa
        
        📊 Complexity:
        - Time: O(n + m) - mỗi ký tự chỉ được xét tối đa 2 lần
        - Space: O(m) - lưu bảng LPS
        """
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
            
        # Bước 1: Xây dựng bảng LPS (Longest Prefix Suffix)
        lps = self._buildLPS(needle)
        
        # Bước 2: Tìm kiếm với KMP
        i = 0  # Con trỏ cho haystack
        j = 0  # Con trỏ cho needle
        
        while i < len(haystack):
            if haystack[i] == needle[j]:
                # Match! Tiến cả 2 con trỏ
                i += 1
                j += 1
                
                if j == len(needle):
                    # Tìm thấy toàn bộ needle!
                    return i - j
            else:
                # Mismatch!
                if j > 0:
                    # Nhảy thông minh: dùng LPS để không check lại phần đã match
                    j = lps[j - 1]
                else:
                    # j = 0, không thể nhảy, tiến i
                    i += 1
        
        return -1
    
    def _buildLPS(self, pattern):
        """
        Xây dựng bảng LPS (Longest Prefix Suffix)
        
        LPS[i] = độ dài của prefix dài nhất cũng là suffix của pattern[0:i+1]
        
        Ví dụ: pattern = "aaab"
        - LPS[0] = 0  (chỉ có 'a', không có proper prefix/suffix)
        - LPS[1] = 1  ('aa' có prefix 'a' = suffix 'a')
        - LPS[2] = 2  ('aaa' có prefix 'aa' = suffix 'aa')
        - LPS[3] = 0  ('aaab' không có prefix nào = suffix)
        
        Kết quả: [0, 1, 2, 0]
        """
        m = len(pattern)
        lps = [0] * m
        
        length = 0  # Độ dài của prefix đang xét
        i = 1       # Bắt đầu từ index 1 (LPS[0] luôn = 0)
        
        while i < m:
            if pattern[i] == pattern[length]:
                # Ký tự match, mở rộng prefix
                length += 1
                lps[i] = length
                i += 1
            else:
                # Không match
                if length > 0:
                    # Thử prefix ngắn hơn
                    length = lps[length - 1]
                else:
                    # Không có prefix nào match
                    lps[i] = 0
                    i += 1
        
        return lps


if __name__ == "__main__":
    sol = Solution()
    
    print("=" * 50)
    print("BRUTE FORCE APPROACH:")
    print("=" * 50)
    print(f"'sadbutsad', 'sad'  -> {sol.strStr('sadbutsad', 'sad')}")   # 0
    print(f"'leetcode', 'leeto' -> {sol.strStr('leetcode', 'leeto')}")  # -1
    print(f"'aaaab', 'aaab'     -> {sol.strStr('aaaab', 'aaab')}")      # 1
    
    print()
    print("=" * 50)
    print("KMP ALGORITHM:")
    print("=" * 50)
    print(f"'sadbutsad', 'sad'  -> {sol.strStr_KMP('sadbutsad', 'sad')}")   # 0
    print(f"'leetcode', 'leeto' -> {sol.strStr_KMP('leetcode', 'leeto')}")  # -1
    print(f"'aaaab', 'aaab'     -> {sol.strStr_KMP('aaaab', 'aaab')}")      # 1
    
    # Edge cases
    print()
    print("=" * 50)
    print("EDGE CASES:")
    print("=" * 50)
    print(f"'', ''              -> {sol.strStr_KMP('', '')}")              # 0
    print(f"'a', ''             -> {sol.strStr_KMP('a', '')}")             # 0
    print(f"'', 'a'             -> {sol.strStr_KMP('', 'a')}")             # -1
