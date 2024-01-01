class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {
        1: 'I',4: 'IV',
        5: 'V', 9: 'IX',
        10: 'X',40: 'XL',
        50: 'L', 90: 'XC',
        100: 'C',400: 'CD',
        500: 'D',900: 'CM',
        1000: 'M'}

        roman = ''
        while num >= 1:
            for value in list(romans.keys())[::-1]:
                    if num - value >= 0:
                        num-=value
                        roman+=romans[value]
                        break
        return roman