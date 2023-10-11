class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start_x, start_y, offset = 0, 0, 1
        count = 1
        #res = []
        #for _ in range(n):
            #res.append([0]*3)
        res = [[0]*n for _ in range(n)]
        for _ in range(n//2):
            x = n - offset
            y = n - offset
            for j in range(start_y, y):
                res[start_x][j] = count
                count += 1
            for i in range(start_x, x):
                res[i][y] = count
                count += 1
            for j in range(y, start_y, -1):
                res[x][j] = count
                count += 1
            for i in range(x, start_x, -1):
                res[i][start_y] = count
                count += 1
            start_x += 1
            start_y += 1
            offset += 1
        if n%2 == 1:
            res[n//2][n//2] = n**2
        return res
