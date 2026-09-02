class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        seen = set()
        i = 0

        for j in range(len(s)):
            while s[j] in seen:
                    seen.remove(s[i])
                    i += 1
            seen.add(s[j])
            maxlength = max(j-i+1, maxlength)
        
        return maxlength