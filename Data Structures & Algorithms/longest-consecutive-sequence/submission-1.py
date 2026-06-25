class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set()
        for x in nums:
            if x in seen:
                continue
            else:
                seen.add(x)
        count = 1
        maxCount = 1
        for x in nums:
            t = 1
            while x + t in seen:
                count += 1
                t += 1
            if count > maxCount:
                maxCount = count
            count = 1
        return maxCount