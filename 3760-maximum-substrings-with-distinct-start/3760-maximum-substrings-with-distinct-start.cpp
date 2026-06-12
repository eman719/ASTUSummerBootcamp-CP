class Solution {
public:
    int maxDistinct(string s) {
        bool seen[26] = {false};
        int distinct_count = 0;
        
        for (char c : s) {
            int index = c - 'a';
            if (!seen[index]) {
                seen[index] = true;
                distinct_count++;
            }
        }
        
        return distinct_count;
    }
};