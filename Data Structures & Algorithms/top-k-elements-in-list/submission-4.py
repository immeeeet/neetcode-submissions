class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for i in nums:
            d[i] = d.get(i,0) + 1
        arr = sorted(d.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i][0])

        return ans
