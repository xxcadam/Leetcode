class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        while True:
            if num >= 1000:
                result += "M" * int(num/1000)
                num = num % 1000
            elif num >= 900:
                result += "CM"
                num = num % 900
            elif num >= 500:
                result += "D"
                result += "C" * int((num - 500)/100)
                num = num % 100
            elif num >= 400:
                 result += "CD"
                 num = num % 100
            elif num >= 100:
                result += "C" * int(num/100)
                num = num % 100
            elif num >= 90:
                result += "XC"
                num = num % 10
            elif num >= 50:
                result += "L"
                result += "X" *int((num-50)/10)
                num = num % 10
            elif num >= 40:
                result += "XL"
                num = num%10
            elif num >= 10:
                result += "X"*int(num/10)
                num = num % 10
            elif num >= 9:
                result += "IX"
                break
            elif num >= 5:
                result += "V"
                result += "I"*int(num-5)
                break
            elif num >= 4:
                result += "IV"
                break
            elif num >= 0:
                result += "I" * int(num - 0)
                break
        return result