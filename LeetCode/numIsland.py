class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return

        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)


input_list = [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]]
for i in input_list:
    print(Solution().numIslands(i))