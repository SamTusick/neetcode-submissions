class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        ans = []

        for i in range (0, len(nums)):
            diff = target - nums[i]
            if diff not in myDict:
                myDict[nums[i]] = i
            else:
                ans.append(myDict[diff])
                ans.append(i)
        return ans
        