class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr, total = 0,0
        prevs = {0:1}
        
        for n in nums:
            curr = curr + n
            if curr - k in prevs:
                total = total + prevs[curr - k]

            if curr in prevs:
                prevs[curr] += 1
            else:
                prevs[curr] = 1
        return total

