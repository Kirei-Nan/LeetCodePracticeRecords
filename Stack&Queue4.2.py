class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                temp=stack.pop()
                print(temp)
                if s[i]==")":
                    if temp !="(":
                        return False
                elif s[i]=="]":
                    if temp !="[":
                        return False
                elif s[i]=="}":
                    if temp != "{":
                        return False
        return not stack