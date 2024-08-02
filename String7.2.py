class Solution:
    def getNext(self,next,s):
        next[0]=0
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
        next=[0]*len(s)
        self.getNext(next,s)
        minunit=len(s)-next[-1]
        return True if len(s)%minunit==0 and minunit!=len(s) else False