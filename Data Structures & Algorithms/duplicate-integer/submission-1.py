class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initiate dict 
        shown = {}
        # intitate res(bool)
        res = False
        # loop through nums 
        for num in nums:
        # if num not in dict
            if num not in shown:
            # add to dict 
                shown[num] = 1
            else:
                return True
        # return res
        return res