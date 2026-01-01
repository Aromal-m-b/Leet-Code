class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number =int("".join(map(str, digits))) + 1
        digits = list(map(int, str(number)))
        return digits