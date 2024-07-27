class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record={}
        for c1 in s:
            record[c1]=record.get(c1,0)+1
        for c2 in t:
            record[c2]=record.get(c2,0)-1
        for i in record.values():
            if i !=0:
                return False
        return True

