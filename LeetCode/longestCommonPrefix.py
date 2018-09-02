class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs) is None:
            return ""
        counter = 0
        min_len = pow(2, 31) - 1
        flag = False
        for str in strs:
            temp = len(str)
            if temp < min_len:
                min_len = temp

        while counter < min_len:
            temp_str = strs[0][counter]
            for str in strs:
                if str[counter] is temp_str:
                    flag = True
                else:
                    flag = False
                    break
            if flag is True:
                counter += 1
            else:
                break

        return strs[0][0:counter]


sample_list = [["c","acc","ccc"]]

for sample in sample_list:
    print(Solution().longestCommonPrefix(sample))