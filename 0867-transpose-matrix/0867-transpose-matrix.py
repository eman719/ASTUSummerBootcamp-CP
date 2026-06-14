class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        R = len(matrix)
        C = len(matrix[0])
        
        # Create a blank result matrix of dimensions C x R
        result = [[0] * R for _ in range(C)]
        
        for r in range(R):
            for c in range(C):
                result[c][r] = matrix[r][c]
                
        return result
    