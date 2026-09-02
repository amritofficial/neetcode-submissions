class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        target = 0

        for i in range(len(nums)-1):
            j = i+1
            k = len(nums) -1
            while j < k:
                summ = nums[i]+nums[j]+nums[k]
                if summ == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif summ < target:
                    j +=1
                else:
                    k -=1
        
        return list(s)