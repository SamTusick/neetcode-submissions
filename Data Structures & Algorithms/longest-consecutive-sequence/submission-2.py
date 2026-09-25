class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # initiate hash
        vals = {}
        max_len = 0

        # store arr in hash 
        for num in nums:
           if num not in vals:
            vals[num] = 0

        # traverse org. arr checking if num - 1 exists
        for num in nums:
            if num - 1 in vals:
                continue
            else:
                # if DNE start sequence
                # check if num + 1 exists
                length = 1
                while num + 1 in vals:
                    length += 1
                    num += 1

            if length > max_len:
                max_len = length

        return max_len