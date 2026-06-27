class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(numbers):
            d[n]=i

        for i in numbers:
            k = target-i
            if k in numbers:
                return [d[i]+1,d[k]+1]