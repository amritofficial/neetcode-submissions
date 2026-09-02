class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapp = defaultdict(int)
        
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mapp[tmp]:
                return [mapp[tmp], i+1]
            mapp[numbers[i]] = i+1
        
        return []