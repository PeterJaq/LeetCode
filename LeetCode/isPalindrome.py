import math


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        str_x = list(str(x))
        len_x = len(str_x)


        if len_x % 2 is 0:
            mid_idx = math.ceil(len(str_x) / 2) -1
            left = str_x[0:mid_idx + 1]
            right = str_x[mid_idx+1:len_x]
            print(mid_idx, left, right[::-1])
            if left == right[::-1]:
                return True
            else:
                return False
        else:
            mid_idx = math.ceil(len(str_x) / 2) - 1
            left = str_x[0:mid_idx + 1]
            right = str_x[mid_idx:len_x]
            print(left, right[::-1])
            if left == right[::-1]:
                return True
            else:
                return False

example_list = ["121", "10", "1010","111"]
for input_str in example_list:
    print(Solution().isPalindrome(input_str))