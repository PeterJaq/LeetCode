class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        self.dfs(nums, res)

        return res

    def dfs(self, nums, res):
        if nums not in res:
            res.append(nums)

        if len(nums) == 1:
            return

        for i in range(len(nums)):
            path = nums[:]
            path.pop(i)
            self.dfs(path, res)


print(Solution().subsets([1,2,3]))