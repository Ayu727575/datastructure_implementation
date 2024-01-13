# https://practice.geeksforgeeks.org/contest/gfg-weekly-coding-contest-135/problems
from typing import List


class Solution:
    def maximum_energy(self, n : int, heights : List[int]) -> int:
        # code here
        nxt_greater_element = [0]*n
        stk = []
        dp = [-1]*n
        ans = 0
        i = n-1
        while i>=0:
            while stk and heights[stk[-1]]<heights[i]:
                stk.pop(-1)
            if len(stk) == 0:
                nxt_greater_element[i] = -1
            else:
                nxt_greater_element[i] = stk[-1]
            stk.append(i)
            i-=1
        for i in range(n-1,-1,-1):
            if nxt_greater_element[i] == -1:
                dp[i] = heights[i]
            else:
                dp[i] = heights[i]^dp[nxt_greater_element[i]]
            ans = max(ans, dp[i])
        return ans