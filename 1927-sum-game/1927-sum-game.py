class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        mid=n//2

        leftSum=0
        rightSum=0
        leftQ=0
        rightQ=0

        #first half
        for ch in num[:mid]:
            if ch=='?':
                leftQ+=1
            else:
                leftSum+=int(ch)

        #right half
        for ch in num[mid:]:
            if ch=='?':
                rightQ+=1
            else:
                rightSum+=int(ch)

         # Odd number of '?' => Alice wins
        if (leftQ + rightQ) % 2 == 1:
            return True

        # Check whether Bob can perfectly balance both sides
        if leftSum - rightSum == (rightQ - leftQ) * 9 // 2:
            return False

        return True
        