class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in bracket_map.values():
                # It's an opening bracket, push onto the stack
                stack.append(char)
            elif char in bracket_map:
                # It's a closing bracket, check for a matching opening bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                # If the character is not a bracket (optional based on constraints)
                return False
        return not stack  # Return True if stack is empty (all brackets matched)
