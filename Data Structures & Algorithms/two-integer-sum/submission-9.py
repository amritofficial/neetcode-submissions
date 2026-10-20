class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        result = []

        for i in range(len(nums)):
            if target - nums[i] in count.values():
                result.append(nums.index(target-nums[i]))
                result.append(i)
            count[i] = nums[i]
        
        return result