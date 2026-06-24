class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sNums = sorted(nums)

        for i in range(len(sNums)):
            for j in range(len(sNums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        if i > j:
                            return [j,i]
                        else:
                            return [i,j]