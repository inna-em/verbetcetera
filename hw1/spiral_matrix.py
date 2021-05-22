class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        w = len(matrix[0])
        h = len(matrix)
        num_layers = min(w, h) // 2
        for n in range(num_layers):
            for i in range(n, len(matrix[0])-n):
                result.append(matrix[n][i])
            for j in range(n+1, len(matrix)-n):
                result.append(matrix[j][-1-n])
            for i in range(len(matrix[0])-2-n, n-1, -1):
                result.append(matrix[len(matrix)-1-n][i])
            for j in range(len(matrix)-2-n, n, -1):
                result.append(matrix[j][n])
        if min(w, h)%2 != 0:
            last_index = num_layers
            for i in range(last_index, max(w,h) - last_index):
                if w >= h:
                    result.append(matrix[last_index][i])
                else:
                    result.append(matrix[i][last_index])
        return result
