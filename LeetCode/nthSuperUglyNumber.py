class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
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

sample_list = [[2, 7, 13, 19]]
n = 12
for sample in sample_list:
    print(Solution().nthSuperUglyNumber(n, sample))