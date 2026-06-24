class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            if x not in count:
                count[x] = 0
            count[x] += 1
        kCount = list(count.items())
        kCount.sort(key=lambda item:item[1], reverse=True)
        result = []
        for item in kCount[:k]:
            result.append(item[0])
        return result
        