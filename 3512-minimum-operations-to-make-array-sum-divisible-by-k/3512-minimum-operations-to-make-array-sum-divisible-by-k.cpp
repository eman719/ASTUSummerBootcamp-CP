class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
       long long total_sum = 0;
        
        for (int num : nums) {
            total_sum += num;
        }
        
        return total_sum % k; 
    }
};