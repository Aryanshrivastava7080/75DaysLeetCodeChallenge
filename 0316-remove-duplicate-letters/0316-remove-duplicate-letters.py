class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}

        # Har character ki last position store karo
        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            # Agar character already stack me hai, skip
            if ch in seen:
                continue

            # Stack ke top ko remove karo agar:
            # 1. top current character se bada hai
            # 2. top character future me dobara available hai
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)
      