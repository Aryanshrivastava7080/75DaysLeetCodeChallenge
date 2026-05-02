class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(
            any(c in '2569' for c in s) and not any(c in '347' for c in s)
            for s in map(str, range(1, n+1))
        )
        