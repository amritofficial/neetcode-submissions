class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for currentIndex, currentTemp in enumerate(temperatures):
            while stack and currentTemp > stack[-1][0]:
                lastTemp, lastIndex = stack.pop()
                res[lastIndex] = currentIndex-lastIndex
            stack.append([currentTemp, currentIndex])
        return res