class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0

        min_len = float('inf')
        ans = ""

        for right in range(len(s)):

            if s[right] == '1':
                ones += 1

            # Agar k se zyada 1 ho gaye
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # Exactly k ones
            if ones == k:

                # Leading extra zeros remove karo
                while s[left] == '0':
                    left += 1

                curr = s[left:right + 1]
                curr_len = len(curr)

                if curr_len < min_len:
                    min_len = curr_len
                    ans = curr

                elif curr_len == min_len and curr < ans:
                    ans = curr

        return ans