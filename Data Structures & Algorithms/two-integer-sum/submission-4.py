class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        result = []

        for i in range(len(nums)):
            if target - nums[i] in mapp.values():
                result.append(nums.index(target-nums[i]))
                result.append(i)
            mapp[i] = nums[i]

        return result