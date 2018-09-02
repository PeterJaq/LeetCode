class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        Flag = True
        if num is 1:
            return True
        if num <= 0 or num > pow(2, 31) - 1:
            return False

        while(abs(num) > 1 and Flag is True):
            Flag = False
            if num % 2 == 0:
                num = num / 2
                Flag = True
            if num % 3 == 0:
                num = num / 3
                Flag = True
            if num % 5 == 0:
                num = num / 5
                Flag = True

        if Flag is True:
            return True
        else:
            return False



sample_list = [-1000]

for sample in sample_list:
    print(Solution().isUgly(sample))