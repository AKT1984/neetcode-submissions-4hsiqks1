class Solution:
    def isValid(self, s: str) -> bool:
        # Eliminate odd number of brackets
        if len(s) & 1:
            return False

        stack = []
        
        for br in s:
            match br:
                case '}':
                    if not stack or stack.pop() != '{':
                        return False
                case ']':        
                    if not stack or stack.pop() != '[':
                        return False
                case ')':        
                    if not stack or stack.pop() != '(':
                        return False
                case _:
                    stack.append(br)
        return not stack                 
                    
