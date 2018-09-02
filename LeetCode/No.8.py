class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        num_list = ['0','1','2','3','4','5','6','7','8','9','0']
        all_list = ['+','-','0','1','2','3','4','5','6','7','8','9','0']
        max_num = pow(2, 31) - 1
        min_num = -pow(2, 31)
        temp = []

        if str is None or len(str) == 0:
            return 0
        if str[0] is '-' and len(str) == 1:
            return 0

        if str[0] in all_list:
            if str[0] is '-':
                for num in range(1, len(str)):
                    if str[num] not in num_list:
                        break
                    temp.append(str[num])
                if len(temp) == 0:
                    return 0
                new_str = int('-' + ''.join(temp))
                if new_str < min_num:
                    return min_num
                else:
                    return new_str
            elif str[0] is '+':
                for num in range(1, len(str)):
                    if str[num] not in num_list:
                        break
                    temp.append(str[num])
                new_str = int(''.join(temp))
                if new_str > max_num:
                    return max_num
                else:
                    return new_str
            else:
                for num in range(0, len(str)):
                    if str[num] not in num_list:
                        break
                    temp.append(str[num])
                new_str = int(''.join(temp))
                if new_str > max_num:
                    return max_num
                else:
                    return new_str
        else:
            return 0

        #for i in enumerate(str):
        #    if i in


example_list = ["   +0 123","+1","-+1", "-", "", "42", "   -42", "4193 with words",  "words and 987", "-91283472332"]
for input_str in example_list:
    print(Solution().myAtoi(input_str))