class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }

        stack = []

        for c in s:
            """
            if open:
                add c to stack
                continue
            if close:
                if stack[-1] == hashmap[c]:
                    stack.pop()
            """

            # If c is an opening bracket, add it to the stack
            if c not in hashmap:
                stack.append(c)
                continue
            else:
                # If the stack is empty or the top of the stack does not match
                # the expected opening bracket, return False
                if not stack or stack[-1] != hashmap[c]:
                    return False
                stack.pop()  # Remove the matched opening bracket from the stack
        
        # Return True if stack is empty, indicating all brackets are matched
        return not stack
