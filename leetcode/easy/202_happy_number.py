class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        result = set()
        while n != 1:
            if n in result:
                return False
            result.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return True