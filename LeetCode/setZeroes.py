class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        lenRow = len(matrix[0])
        lenLine = len(matrix)

        zeroRow = [False] * lenRow
        zeroLine = [False] * lenLine

        for l in range(lenLine):
            for r in range(lenRow):
                if matrix[l][r] == 0:
                    zeroRow[r] = True
                    zeroLine[l] = True

        for l in range(lenLine):
            if zeroLine[l] is True:
                matrix[l] = [0] * lenRow
            else:
                for r in range(lenRow):
                    if zeroRow[r] is True:
                        matrix[l][r] = 0

        return matrix


sample_list = [[[0,1,2,0], [3,4,5,2], [1,3,1,5]]]
n = 12
for sample in sample_list:
    print(Solution().setZeroes(sample))