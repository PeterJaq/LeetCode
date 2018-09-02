class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_ans = 0
        while(left < right):
            value = (right - left) * min(height[left], height[right])
            print(value)
            if(max_ans < value):
                max_ans = value

            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return max_ans



example_list = [[1,8,6,2,5,4,8,3,7]]
for input in example_list:
    print(Solution().maxArea(input))