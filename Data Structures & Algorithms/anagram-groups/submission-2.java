class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for (String s: strs) {
            char[] characters = s.toCharArray();
            Arrays.sort(characters);
            String sortedWord = new String(characters);

            if (!anagrams.containsKey(sortedWord)){
                anagrams.put(sortedWord, new ArrayList<>());
            }
            anagrams.get(sortedWord).add(s);
        }
        return new ArrayList<>(anagrams.values());
    }
}
