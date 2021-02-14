class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        for e in s:
            if e == " ":
                i += 1
            else:
                s = s[i:]
                break
        if not s:
            return 0
        negative = 1
        if s[0] == "-":
            s = s[1:]
            negative = -1
        elif s[0] == "+":
            s = s[1:]
            negative = 1

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -1 * (INT_MAX + 1)
        if len(s) == 0:
            return 0
        result = 0
        for i in range(len(s)):
            if "0" <= s[i] <= "9":
                if negative * (result * 10 + int(s[i])) < INT_MIN:
                    return INT_MIN
                elif negative * (result * 10 + int(s[i])) > INT_MAX:
                    return INT_MAX
                else:
                    result = result * 10 + int(s[i])
            else:
                if i == 0:
                    return 0
                break

        return result * negative


if __name__ == '__main__':
    a = Solution()
    print(a.myAtoi("4193 with words"))