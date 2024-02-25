class Solution(object):
    def isValid(self,startIndex,endIndex,s):
        if startIndex > endIndex:
            return False
        if int(s[startIndex]) ==0 and startIndex<endIndex :
            return False
        for i in range(startIndex,endIndex+1):
            if not s[i].isdigit():
                return False
        if int(s[startIndex:endIndex+1])>255 or int(s[startIndex:endIndex+1])<0:
            return False
        return True
    def backtrack(self,s,pointsum,startIndex,path,result):
        if pointsum ==3:
            if self.isValid(startIndex,len(s)-1,s):
                result.append(path+(s[startIndex:len(s)]))
                return
        for i in range(startIndex,len(s)):
            if self.isValid(startIndex,i,s):
                pointsum+=1
                self.backtrack(s,pointsum,i+1,path+(s[startIndex:i+1]+"."),result)
                pointsum-=1


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result=[]
        self.backtrack(s,0,0,"",result)
        return result