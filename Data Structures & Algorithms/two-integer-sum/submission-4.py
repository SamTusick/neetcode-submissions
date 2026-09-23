class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store diff in hashmap
        # traverse through array
        # diff = target - value
        # store diff = index of value
        # if diff in hash
        # return both indicies 

        diff_val = {}
        ans = []

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff not in diff_val:
                diff_val[nums[i]] = i
            else:
                ans.append(diff_val[diff])
                ans.append(i)
        return ans


