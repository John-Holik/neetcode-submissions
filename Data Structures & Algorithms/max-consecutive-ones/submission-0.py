class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for x in nums:
            if x == 1:
                count += 1
            if x == 0:
                if count > maxCount:
                    maxCount = count
                count = 0
            if count > maxCount:
                    maxCount = count
        return maxCount