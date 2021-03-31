class Solution:
    def longestCommonPrefix(self, strs) -> str:
        result = ""
        l = len(strs)
        if l == 1:
            return strs[0]
        j = 0
        while True:
            try:
                for i in range(0, l - 1):
                    if strs[i][j] == strs[i + 1][j]:
                        continue
                    return result
            except:
                break
            result += strs[0][j]
            j += 1

        return result


if __name__ == '__main__':
    a = Solution()
    print(a.longestCommonPrefix(["flower", "flow", "flaw"]))