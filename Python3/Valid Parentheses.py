class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for e in s:
            if e == '{' or e == '(' or e == '[':
                stack.append(e)
            elif e == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif e == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif e == ')':
                if not stack or stack.pop() != '(':
                    return False
            else:
                continue

        if not stack:
            return True
        else:
            return False