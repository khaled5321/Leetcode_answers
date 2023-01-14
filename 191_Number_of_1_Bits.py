class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        lst = list(map(int, binary))

        return sum(lst)
