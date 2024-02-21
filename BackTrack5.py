class Solution(object):
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
    def backtracking(self, digits,index,result,str):
        if len(digits) == len(str):
            result.append(str)
            return
        digit=int(digits[index])
        letters=self.letterMap[digit]
        for i in range(len(letters)):
            str+=letters[i]
            self.backtracking(digits, index+1, result,str)
            str=str[:-1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if len(digits)==0:
            return result

        self.backtracking(digits,0,result,"")
        return result