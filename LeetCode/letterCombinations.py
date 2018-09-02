class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [i for i in digit2chars[digits[0]]]

        for i in digits[1:]:
            res = [m + n for m in res for n in digit2chars[i]]

        return res

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        shuju = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        digits = list(digits)
        res = []
        while digits:
            a = digits.pop(0)
            if res == []:  # 如果res没有值直接加进去
                for i in shuju[a]:
                    res.append(i)

            else:
                temp = []
                for i in shuju[a]:
                    temp += list(map(lambda x: x+i, res))
                res = temp
        return res

print(Solution().letterCombinations("234"))
print(Solution().letterCombinations2("234"))