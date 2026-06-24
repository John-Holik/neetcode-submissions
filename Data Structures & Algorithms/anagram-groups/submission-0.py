class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            srtd = "".join(sorted(word))
            if srtd in d:
                d[srtd].append(word)
            else:
                d[srtd] = [word]
        return list(d.values())