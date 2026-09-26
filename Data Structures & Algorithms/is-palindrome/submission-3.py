class Solution:
    # Valid Char ([0-9]48-57,[A-Z]65-90,[a-z]97-122)
    def isValidChar(self, c) -> bool:
        if 48 <= ord(c) <= 57 or 97 <= ord(c) <= 122:
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            if not self.isValidChar(s[l]):
                l += 1
                continue
            if not self.isValidChar(s[r]):
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
            
        