class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) < 3 or nums is None:
            return False
        one = pow(2, 32) -1
        second = pow(2, 32) - 1

        for num in nums:
            if num <= one:
                one = num
            elif num <= second and num > one:
                second = num
            else:
                return True

        return False



sample_list = [[1,2,3,4,5], [5,4,3,2,1],[2,1,5,0,4,6],[1,1,1,1,1,1]]
for sample in sample_list:
    print(Solution().increasingTriplet(sample))