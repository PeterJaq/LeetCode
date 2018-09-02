class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1: return [nums]
        if len(nums) == 2: return [nums, [nums[-1],nums[0]]]
        res = []
        for i in range(len(nums)):
            rest = nums[:]
            print(rest)
            rest.pop(i)
            for j in self.permute(rest):
                res.append([nums[i]] + j)
                res.append([nums[i]])
        return res

print(Solution().permute([1,2,3]))