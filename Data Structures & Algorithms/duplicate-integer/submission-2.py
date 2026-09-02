class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        resultSet = set()

        for n in nums:
            if n in resultSet:
                return True
            resultSet.add(n)

        return False