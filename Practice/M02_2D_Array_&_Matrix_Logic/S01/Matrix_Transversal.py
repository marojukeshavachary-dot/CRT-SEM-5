'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = 0
        
        for i in range(n):
            total_sum += mat[i][i]  
            total_sum += mat[i][n - 1 - i]  
            
        
        if n % 2 == 1:
            total_sum -= mat[n // 2][n // 2]
            
        return total_sum

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))


# 498 - Diagonal Traverse
class Solution:
    def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
        rows,cols = len(mat),len(mat[0])
        res = []
        for d in range(rows + cols - 1):
            diagonal = []
            r = 0 if d < cols else d - cols + 1 
            c = d if d < cols else cols - 1 
            while r < rows and c >= 0:
                diagonal.append(mat[r][c])
                r += 1 
                c -= 1 
            if d % 2 == 0:
                diagonal.reverse()
            res += diagonal 
        return res
        
        '''