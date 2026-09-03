class Solution {
public:
    bool check(vector<int>& nums) {
        int count = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            // Cyclically check: compare current element with next element
            if (nums[i] > nums[(i + 1) % n]) {
                count++;
            }
        }

        // Agar drop 1 ya 0 baar hua hai toh true
        return count <= 1;
    }
};