class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [0] * numRows
        for i in range(numRows):
            output[i] = [1] * (i+1)

            for j in range(1, i):
                output[i][j] = output[i-1][j-1] + output[i-1][j]


        return output
