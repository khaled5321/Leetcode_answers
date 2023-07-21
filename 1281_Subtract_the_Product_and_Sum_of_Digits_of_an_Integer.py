import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list_of_numbers = [int(x) for x in str(n)]

        product = math.prod(list_of_numbers)
        _sum = sum(list_of_numbers)

        return product - _sum
