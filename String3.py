class Solution:
    def replace(self,s:str)->str:
        res=list(s)
        for i in range(len(res)):
            if res[i].isdigit():
                res[i]="nums"
        return ''.join(res)

sol=Solution()
s=input()
result=sol.replace(s)
print(result)
