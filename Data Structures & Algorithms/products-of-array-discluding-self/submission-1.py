class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_counter = 0
        zero_index = None
        ans = []

        for i, num in enumerate(nums):
            if num == 0:
                zero_counter += 1
                zero_index = i
            else:
                total = total * num
        for j, num in enumerate(nums):
            if zero_counter == 1:
                if j == zero_index:
                    val = total
                else: 
                    val = 0
            elif zero_counter > 1:
                return [0] * len(nums)
            else:
                val = int(total / num)
            ans.append(val)
        return ans

        