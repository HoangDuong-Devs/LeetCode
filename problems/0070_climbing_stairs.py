"""
================================================================================
LeetCode #70: Climbing Stairs
================================================================================
Difficulty: Easy
Date Started: 2025-12-13
Link: https://leetcode.com/problems/climbing-stairs/

--------------------------------------------------------------------------------
Description:
--------------------------------------------------------------------------------
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you 
climb to the top?

--------------------------------------------------------------------------------
Examples:
--------------------------------------------------------------------------------
Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

--------------------------------------------------------------------------------
💡 Hints (Gợi ý):
--------------------------------------------------------------------------------
1. Đây là bài toán Fibonacci: ways(n) = ways(n-1) + ways(n-2)
2. Base cases: ways(1)=1, ways(2)=2
3. Có thể dùng DP hoặc recursive với memo để tránh TLE

--------------------------------------------------------------------------------
🎯 Approach gợi ý: Dynamic Programming
--------------------------------------------------------------------------------
Dùng array dp[n+1], dp[1]=1, dp[2]=2
For i from 3 to n: dp[i] = dp[i-1] + dp[i-2]
Return dp[n]

⏰ Time Complexity mục tiêu: O(n)
💾 Space Complexity mục tiêu: O(n) hoặc O(1) nếu optimize
"""

class Solution(object):
    
    def factorial(self, x):
        if x == 0: return 1
        return x * self.factorial(x-1)
    
    def chosennumber(self, round, position):
        if round == 0: return 1
        return position * self.chosennumber(round-1, position-1) 
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        round = n // 2
        paths = 0
        while(round >= 0):
            position = n - round    
            paths += self.chosennumber(round, position) / self.factorial(round)
            round -= 1
            pass
            
        return paths
    
    def climbStairs_v2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        return self.climbStairs_v2(n-1) + self.climbStairs_v2(n-2)

if __name__ == "__main__":
    sol = Solution()
    # Test cases - uncomment khi đã implement
    print(sol.climbStairs(11))     # Expected: 2
    print(sol.climbStairs_v2(11))  # Expected: 3
    print(sol.climbStairs(0))