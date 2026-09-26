class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        
        for char in s:
            if char == '(' or char == '[' or char == '{':
                open_stack.append(char)
            elif (char == ')' or char == ']' or char == '}') and len(open_stack) > 0:
                check = open_stack.pop()
                if (check == '(' and char == ')') or (check == '[' and char == ']') or (check == '{' and char == '}'):
                    continue 
                else:
                    return False
            else:
                return False
        return len(open_stack) == 0 