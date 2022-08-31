class Solution1:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [int(x) for x in str(int(''.join(str(x) for x in digits))+1)]


class Solution2:
    def plusOne(self, digits: list[int]) -> list[int]:
        l = len(digits)
        digits.insert(0, 0)
        for i, x in enumerate(digits[::-1]):
            if x+1 > 9:
                digits[l-i] = 0
            else:
                digits[l-i] += 1
                break
        if digits[0] == 0:
                digits.pop(0)
        return digits


class Solution3:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i]+1 > 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1]+digits
