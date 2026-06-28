class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(numbers):
            k = target - n
            if k in d:
                return [d[k]+1, i+1]   # +1 because problem expects 1-based indexing
            d[n] = i
        return []