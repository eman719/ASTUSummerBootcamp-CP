class Solution {
public:
    int countDigitOccurrences(vector<int>& nums, int digit) {
        int count = 0;
        for (int num : nums) {
            if (num == 0 && digit == 0) {
                count++;
                continue;
            }
            int temp = abs(num);
            while (temp > 0) {
                if (temp % 10 == digit) {
                    count++;
                }
                temp /= 10;
            }
        }
        return count;
    }
};