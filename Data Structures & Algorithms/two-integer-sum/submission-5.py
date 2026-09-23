class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store diffs in hash
        diffs = {}
        # store ans in set
        ans = []

        for i in range(len(nums)):
            if nums[i] not in diffs:
                diffs[target - nums[i]] = i
            else:
                ans.append(diffs[nums[i]])
                ans.append(i)
        return ans