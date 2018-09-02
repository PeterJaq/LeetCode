class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num <= 0 or num >= 4000:
            return False
        roman = ""

        while num > 0:
            if num >= 1000:
                roman = roman + "M"
                num -= 1000
            elif num >= 900:
                roman = roman + "CM"
                num -= 900
            elif num >= 500:
                roman = roman + "D"
                num -= 500
            elif num >= 400:
                roman = roman + "CD"
                num -= 400
            elif num >= 100:
                roman = roman + "C"
                num -= 100
            elif num >= 90:
                roman = roman + "XC"
                num -= 90
            elif num >= 50:
                roman = roman + "L"
                num -= 50
            elif num >= 40:
                roman = roman + "XL"
                num -= 40
            elif num >= 10:
                roman = roman + "X"
                num -= 10
            elif num >= 9:
                roman = roman + "IX"
                num -= 9
            elif num >= 5:
                roman = roman + "V"
                num -= 5
            elif num >= 4:
                roman = roman + "IV"
                num -= 5
            elif num >= 1:
                roman = roman + "I"
                num -= 1

            #print(num, roman)
        return roman

example_list = [3, 4, 9, 58, 1994]
for input_str in example_list:
    print(Solution().intToRoman(input_str))