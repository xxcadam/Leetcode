class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i, j = 0, 0
        result = ["" for i in range(numRows)]
        direction = 1
        # direction 1 go down, -1 go up
        for e in s:
            result[i] = result[i] + e
            if direction == 1 and i != numRows - 1:
                i += 1
            elif i == numRows - 1 and direction == 1:
                i -= 1
                direction = -1
            elif direction == -1 and i != 0:
                i -= 1
            elif i == 0 and direction == -1:
                direction = 1
                i += 1
        return ''.join((str(x) for x in result))