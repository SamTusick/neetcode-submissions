class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, res = 0, []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i + 1, len(nums) - 1

            while l<r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else: 
                    # ADD nums[i], nums[l], nums[r] to result
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while r>l and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
               