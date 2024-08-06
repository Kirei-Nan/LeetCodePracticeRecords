class Solution:
    def isvalid(self,s:str)->bool:
        if len(s)==0:
            return False
        if s[0]=='0' and len(s) > 1:
            return False
        for i in range(len(s)):
            if not s[i].isdigit():
                return False
        if int(s)>255 or int(s)<0:
            return False
        return True
    def backtracking(self,s,startIndex,path,result):
        if len(path)==4 and startIndex == len(s):
            result.append(".".join(path))
            return

        for i in range(startIndex,len(s)):
            if self.isvalid(s[startIndex:i+1]):
                path.append(s[startIndex:i+1])
                self.backtracking(s, i + 1, path, result)
                path.pop()
    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        self.backtracking(s,0,[],result)
        return result