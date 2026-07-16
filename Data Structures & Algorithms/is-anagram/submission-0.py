class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict  =  {}
        ans = False

        if len(s) != len(t):
            return False

        for i in range(0,len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = 1
            else: 
                my_dict[s[i]] += 1
        for j in range(0,len(t)):
            if t[j] not in my_dict:
                return False
            else:
                my_dict[t[j]] -= 1
        
        if all(value == 0 for value in my_dict.values()):
            ans = True
        return ans