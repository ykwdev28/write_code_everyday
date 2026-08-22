class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary = format(n, '032b')
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)