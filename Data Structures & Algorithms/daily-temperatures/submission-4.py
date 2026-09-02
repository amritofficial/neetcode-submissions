class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for currentIndex, currentTemp in enumerate(temperatures):
            while stack and currentTemp > stack[-1][1]:
                lastIndex, lastTemp = stack.pop()
                res[lastIndex] = currentIndex - lastIndex
            stack.append([currentIndex, currentTemp])

        return res