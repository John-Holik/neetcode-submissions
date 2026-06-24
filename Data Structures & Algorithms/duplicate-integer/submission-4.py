class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = set()
        for i in range(len(nums)):
            if nums[i] in output:
                return True 
            output.add(nums[i])
        return False
            