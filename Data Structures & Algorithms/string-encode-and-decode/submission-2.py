class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # this will give us the length (number) before the "#"
            res.append(s[j+1: j+1+length]) # start of the word to the end (full string)
            i = j+1+length # end of string
        
        return res