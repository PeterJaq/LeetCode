class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = {}
        temp_strs = []
        ans = [[] for i in range(len(strs))]

        if len(strs) == 1:
            return strs

        for str in strs:
            temp_strs.append(''.join(sorted(list(str))))

        idx_count = -1
        for i in range(len(temp_strs)):
            if temp_strs[i] not in temp:
                idx_count += 1
                temp[temp_strs[i]] = idx_count
                ans[idx_count].append(strs[i])
            else:
                ans[temp[temp_strs[i]]].append(strs[i])

        while [] in ans:
            ans.remove([])

        return ans

tests = [["",""]]
for test in tests:
    print(Solution().groupAnagrams(test))
