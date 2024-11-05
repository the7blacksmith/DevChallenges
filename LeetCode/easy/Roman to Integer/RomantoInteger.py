class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        list_numbers = []
        addition = []
        for x in s[::-1]:
            if x in romans:
                list_numbers.append(romans[x])
        for i, y in enumerate(list_numbers):
            if i == 0:
                addition.append(y)
            elif y < list_numbers[i-1]:
                y = -y
                addition.append(y)
            else:
                addition.append(y)
        return sum(addition)
