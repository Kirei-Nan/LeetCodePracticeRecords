class Solution:
    def isValid(self,s:str,left:int,right:int)->bool:
        if left>right:
            return False
        if s[left]=="0" and left!=right:
            return False
        num=0
        for i in range(left,right+1):
            if not s[i].isdigit():
                return False
            num=num*10+int(s[i])
            if num>255:
                return False
        return True

    def backtracking(self,s:str,path:str,result:List[str],startIndex:int,segments:int):
        if startIndex>=len(s) and segments==4:
            result.append(path[:-1])
            return
        for i in range(startIndex,len(s)):
            if self.isValid(s,startIndex,i):
                self.backtracking(s,path+s[startIndex:i+1]+".",result,i+1,segments+1)


    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        self.backtracking(s,"",result,0,0)
        return result
