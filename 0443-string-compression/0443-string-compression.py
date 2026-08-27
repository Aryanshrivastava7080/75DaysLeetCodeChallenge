class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0       # reading pointer
        index = 0   # writing pointer

        while i < len(chars):
            ch = chars[i]
            count = 0

            # Same consecutive characters count karo
            while i < len(chars) and chars[i] == ch:
                i += 1
                count += 1

            # Character write karo
            chars[index] = ch
            index += 1

            # Agar count > 1 hai to digits bhi write karo
            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1

        return index
        