class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = sorted(s)
        ts = sorted(t)
        return st == ts

        