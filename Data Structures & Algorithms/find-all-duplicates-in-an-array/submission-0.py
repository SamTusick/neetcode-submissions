class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        pass
        ans = []
        repeats = {}

        for n in nums:
            if n not in repeats:
                repeats[n] = 1
            else: 
                ans.append(n)
        return ans
