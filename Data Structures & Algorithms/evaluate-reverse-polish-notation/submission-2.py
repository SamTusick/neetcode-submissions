class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Traverse arr
        # Add to stack
        # Once operator is found
            # Remove last 2 items from stack 
            # Perform operation 
            # Add result to stack
        # Return last item in stack 

        found_stack= []
        operators = '+', '-', '*', '/'

        for val in tokens:
            if val in operators:
                num2 = int(found_stack.pop())
                num1 = int(found_stack.pop())

                if val == '+':
                    result = num1 + num2
                elif val == '-':
                    result = num1 - num2
                elif val == '*':
                    result = num1 * num2
                else: 
                    result = num1 / num2
                found_stack.append(result)
            else:
                found_stack.append(val)
        return int(found_stack.pop())


