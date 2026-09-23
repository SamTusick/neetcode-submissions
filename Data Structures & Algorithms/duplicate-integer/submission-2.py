class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initiate hash 
        seen = {}

        # loop through nums 
        for num in nums:
            # if not in add 
            if num not in seen:
                seen[num] = num
            else:
                return True
        return False