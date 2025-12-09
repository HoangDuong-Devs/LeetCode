"""
================================================================================
LeetCode #14: Longest Common Prefix
================================================================================
Difficulty: Easy
Date Solved: 2025-07-26
Link: https://leetcode.com/problems/longest-common-prefix/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
Write a function to find the longest common prefix string amongst an array 
of strings.

If there is no common prefix, return an empty string "".

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

--------------------------------------------------------------------------------
Solution Approach: Vertical Scanning
--------------------------------------------------------------------------------
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        min_length = min(len(string) for string in strs)

        idx = 0
        res = ""
        
        while idx < min_length:
            char = strs[0][idx]
            for string in strs:
                if string[idx] != char:
                    return res
            res += char
            idx += 1
            
        return res
        

if __name__ == "__main__":
    s = Solution()
    strs = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(strs))  # Output: "fl"
    
    strs2 = ["dog", "racecar", "car"]
    print(s.longestCommonPrefix(strs2))  # Output: ""
