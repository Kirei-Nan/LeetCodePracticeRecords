class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

    def backtracking(self,digits,index,path,result):
        if index==len(digits):
            result.append("".join(path[:]))
            return
        currentIndex=int(digits[index])
        currentButton=self.letterMap[currentIndex]
        for i in range(len(currentButton)):
            path.append(currentButton[i])
            self.backtracking(digits,index+1,path,result)
            path.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        result=[]
        self.backtracking(digits,0,[],result)
        return result