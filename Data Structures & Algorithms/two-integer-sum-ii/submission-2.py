class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        while index1 < index2:
            current = numbers[index1] + numbers[index2]
            if current == target:
                return [index1+1, index2+1]
            elif current > target:
                index2 -= 1
            else:
                index1 += 1