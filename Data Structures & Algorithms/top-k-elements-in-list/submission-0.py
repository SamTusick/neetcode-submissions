class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        sorted_values = sorted(freq.values(), reverse = True)

        target_values = sorted_values[:k]

        result = []

        for key, value in freq.items():
            if value in target_values:
                result.append(key)

        return result

        