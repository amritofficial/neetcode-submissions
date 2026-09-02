class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int n: nums) {
            set.add(n);
        }

        int longest = 0;

        for (int n: nums) {
            if (!set.contains(n-1)) {
                int length = 0;
                while (set.contains(n+length)){
                    length +=1;
                }
                longest = Math.max(length, longest);
            }
        }

        return longest;
    }
}
