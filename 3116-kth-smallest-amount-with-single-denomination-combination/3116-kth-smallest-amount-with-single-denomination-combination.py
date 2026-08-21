from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins, k):
        # Duplicate aur unnecessary coins remove karenge
        coins.sort()
        arr = []

        for coin in coins:
            # Agar coin kisi chhote coin ka multiple hai,
            # to ye unnecessary hai
            if not any(coin % x == 0 for x in arr):
                arr.append(coin)

        coins = arr
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        curr_lcm = lcm(curr_lcm, coins[i])
                        bits += 1

                        # LCM x se bada hai to contribution 0
                        if curr_lcm > x:
                            break

                if curr_lcm > x:
                    continue

                if bits % 2 == 1:
                    ans += x // curr_lcm
                else:
                    ans -= x // curr_lcm

            return ans

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left