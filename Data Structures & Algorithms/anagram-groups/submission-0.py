class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedd = defaultdict(list)

        for s in strs:
            sortedWord = ''.join(sorted(s))
            sortedd[sortedWord].append(s)
        
        return list(sortedd.values())