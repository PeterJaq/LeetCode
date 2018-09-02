class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        edge_max = -pow(2, 31)
        edge_min = pow(2, 31) - 1

        string_int = list(str(x))
        if string_int[0] is '-':
            del (string_int[0])
            new_string = '-' + ''.join(string_int[::-1])
            int_num = int(new_string)
            if int_num <= edge_max:
                return 0
            else:
                return int_num

        else:
            new_string = ''.join(string_int[::-1])
            int_num = int(new_string)
            if int_num >= edge_min:
                return 0
            else:
                return int_num


