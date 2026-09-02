class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()
        for i in range(len(nums) -1):
            if i + 1 < len(nums) and nums[i+1] == nums[i]:
                return True

        return False