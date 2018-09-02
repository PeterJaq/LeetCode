class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2, 3, 5]
        dp = [1]

        lenPrimes = len(primes)
        idxPrimes = [0] * lenPrimes
        counter = 1
        while counter < n:
            min = pow(2, 32)
            for i in range(0, lenPrimes):
                temp = dp[idxPrimes[i]] * primes[i]
                if temp < min:
                    min = temp

            for i in range(0, lenPrimes):
                if min == dp[idxPrimes[i]] * primes[i]:
                    idxPrimes[i] += 1
            dp.append(min)
            counter += 1

        return dp[counter - 1]




n = 10

print(Solution().nthUglyNumber(n))
