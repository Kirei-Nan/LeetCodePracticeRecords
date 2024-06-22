class Solution:
    def getNext(self,s:str,next:List[int])->None:
        j=0
        for i in range(1,len(s)):
            while j>0 and s[i]!=s[j]:
                j=next[j-1]
            if s[i]==s[j]:
                j+=1
            next[i]=j
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)==0:
            return False
        next = [0] * len(s)
        self.getNext(s,next)
        max=next[-1]
        diff=len(s)-max
        if next[-1] != 0 and len(s)%diff==0:
            return True
        return False
