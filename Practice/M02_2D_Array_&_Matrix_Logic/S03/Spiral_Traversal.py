'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top,bottom = 0,n - 1 
        left,right = 0,n - 1 
        res = [[0]*n for _ in range(n)]
        num = 1 
        while top <= bottom and left <= right:
            #left -> right 
            for col in range(left,right+1):
                res[top][col] = num 
                num += 1 
            top += 1 

            #top -> bottom 
            for row in range(top,bottom+1):
                res[row][right] = num 
                num += 1 
            right -= 1

            #right -> left 
            if top <= bottom:
                for col in range(right,left-1,-1):
                    res[bottom][col] = num 
                    num += 1 
                bottom -= 1 

            #bottom -> top 
            if left <= right:
                for row in range(bottom,top-1,-1):
                    res[row][left] = num 
                    num += 1 
                left += 1 
        return res
    
    
    class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        res = []
        
        while top <= bottom and left <= right:
            # 1. Traverse Left -> Right across top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            
            # 2. Traverse Top -> Bottom down rightmost column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            
            # 3. Traverse Right -> Left across bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
            # 4. Traverse Bottom -> Top up leftmost column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
                
        return res
    
    '''