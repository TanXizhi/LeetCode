class Solution:
    def intToRoman(self, num: int) -> str:
        # 从最大数值开始遍历，因此从大到小排列
        pool = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        roman = []
        for value in pool:
            while num >= value:
                num -= value
                roman.append(pool[value])
            if num == 0:
                break
        return "".join(roman)
