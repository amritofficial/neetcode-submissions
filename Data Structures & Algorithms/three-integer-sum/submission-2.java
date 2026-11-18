class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> set = new HashSet<>();
        int target = 0;

        for (int i=0; i < nums.length-1; i++) {
            int j = i+1;
            int k = nums.length-1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == target) {
                    set.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j += 1;
                    k -= 1;
                }
                else if (sum < target) {
                    j += 1;
                }
                else {
                    k -= 1;
                }
            }
        }

        return new ArrayList<>(set);
    }
}
