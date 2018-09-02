class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path, res = "", []
        self.dfs(n, n, res, path)
        return res

    def dfs(self, left, right, res, path):
        if left is 0 and right is 0:
            res.append(path)
            return

        if left > 0:
            self.dfs(left - 1, right, res, path + "(")
        if right > left:
            self.dfs(left, right - 1, res, path + ")")