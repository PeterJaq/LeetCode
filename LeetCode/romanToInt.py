class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dict = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,
        }
        for idx in range(0, len(s) - 1):
            if s[idx] is "C":
                if s[idx+1] is "D" or s[idx+1] is "M":
                    ans -= 100
                else:
                    ans += 100
            elif s[idx] is "X":
                if s[idx+1] is "L" or s[idx+1] is "C":
                    ans -= 10
                else:
                    ans += 10
            elif s[idx] is "I":
                if s[idx+1] is "V" or s[idx+1] is "X":
                    ans -= 1
                else:
                    ans += 1
            elif s[idx] in "V":
                ans += 5
            elif s[idx] in "L":
                ans += 50
            elif s[idx] in "D":
                ans += 500
            elif s[idx] in "M":
                ans += 1000

        ans += dict[s[len(s) - 1]]

        return ans

tests = ["III","IV","IX","LVIII","MCMXCIV"]
for test in tests:
    print(Solution().romanToInt(test))