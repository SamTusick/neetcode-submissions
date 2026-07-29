class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result =  0
        group = set()

        for num in nums:
            group.add(num)
        for n in group:
            if n-1 not in group:
                count = 1
                m = 1
                while n + m in group:
                    count += 1
                    m += 1
                if count > result:
                    result = count
        return result
        