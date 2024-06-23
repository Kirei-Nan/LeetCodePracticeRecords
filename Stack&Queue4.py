class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for item in s:
            if item=="(":
                stack.append(")")
            elif item=="{":
                stack.append("}")
            elif item=="[":
                stack.append("]")
            elif item!=stack[-1] or not stack:
                return False
            else:
                stack.pop()
        return True if not stack else False