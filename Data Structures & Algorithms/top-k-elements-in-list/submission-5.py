class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums)+1)]
        result = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            bucket[c].append(n)
        
        for i in range(len(bucket)-1, -1, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
