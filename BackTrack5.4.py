class Solution:
    def __init__(self):
        self.map={
            0:"",
            1:"",
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
    def backtracking(self,digits,path:str,result,index):
        if len(path)==len(digits):
            result.append(path)
            return
        digit=int(digits[index])
        str=self.map[digit]
        for i in range(len(str)):
            path+=str[i]
            self.backtracking(digits,path,result,index+1)
            path=path[:-1]


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result=[]
        self.backtracking(digits,"",result,0)
        return result