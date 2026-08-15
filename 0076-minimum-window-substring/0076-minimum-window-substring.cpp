class Solution {
public:
    string minWindow(string s, string t) {
       if (s.length() < t.length())
            return "";

        vector<int> freq(128, 0);

        // t ke characters ki frequency
        for (char c : t) {
            freq[c]++;
        }

        int left = 0;
        int right = 0;

        int required = t.length();
        int minLen = INT_MAX;
        int start = 0;

        while (right < s.length()) {

            // Current character window me add kiya
            if (freq[s[right]] > 0) {
                required--;
            }

            freq[s[right]]--;
            right++;

            // Window valid hai
            while (required == 0) {

                // Minimum window update
                if (right - left < minLen) {
                    minLen = right - left;
                    start = left;
                }

                // Left character remove karenge
                freq[s[left]]++;

                if (freq[s[left]] > 0) {
                    required++;
                }

                left++;
            }
        }

        if (minLen == INT_MAX)
            return "";

        return s.substr(start, minLen);
    }
};