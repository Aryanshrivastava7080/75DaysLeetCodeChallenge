class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         count = {}          # character frequency store karega
         left = 0
         max_freq = 0        # window me sabse zyada aane wala character
         max_length = 0

         for right in range(len(s)):
        
        # current character ka count badhao
             count[s[right]] = count.get(s[right], 0) + 1
        
        # maximum frequency update karo
             max_freq = max(max_freq, count[s[right]])

        # check window valid hai ya nahi
             if (right - left + 1) - max_freq > k:
                 count[s[left]] -= 1
                 left += 1

        # maximum substring length update
             max_length = max(max_length, right - left + 1)

         return max_length  
   