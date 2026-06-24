class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = []
        for x in s:
            sList.append(x)
        sList.sort()

        tList = []
        for i in t:
            tList.append(i)
        tList.sort()

        if sList == tList:
            return True
        return False