class Solution {
public:
    int myAtoi(string s) {
        int i = 0;
        int n = s.length();
        int sign = 1;
        long result = 0; // Using long or int with overflow checks

        // Step 1: Skip leading whitespace
        while (i < n && s[i] == ' ') {
            i++;
        }

        // Step 2: Handle optional sign
        if (i < n && (s[i] == '+' || s[i] == '-')) {
            sign = (s[i] == '-') ? -1 : 1;
            i++;
        }

        // Step 3: Parse digits and handle overflow
        while (i < n && isdigit(s[i])) {
            int digit = s[i] - '0';

            // Check overflow before updating result
            if (result > (INT_MAX - digit) / 10) {
                return (sign == 1) ? INT_MAX : INT_MIN;
            }

            result = result * 10 + digit;
            i++;
        }

        return result * sign;
    }
};