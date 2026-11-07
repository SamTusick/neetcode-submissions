class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        types = {}
        best = 0

        for r in range(len(fruits)):
            if fruits[r] not in types:
                types[fruits[r]] = 1
            else:
                types[fruits[r]] += 1

            while len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]
                l += 1

            best = max(best, r - l + 1)
        return best


        