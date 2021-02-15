class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "IV":4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100,
                "CD": 400, "D": 500, "CM": 900, "M": 1000}
        result = 0
        i = 0
        while i < len(s):
            if i <= len(s) - 2:
                if s[i:i+2] in dict.keys():
                    result += dict[s[i:i+2]]
                    i += 2
                    continue
            result += dict[s[i]]
            i += 1

        return result


if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt("III"))
