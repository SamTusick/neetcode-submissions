class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        totals = []
        l,r = 0,0

        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0

        while r != len(s): 
            if s[r] not in substring:
                substring[s[r]] = 1
                r += 1
            else: 
                while s[r] in substring:
                    del substring[s[l]]
                    l += 1
                substring[s[r]] = 1
                r += 1
            totals.append(r-l)
        return max(totals)