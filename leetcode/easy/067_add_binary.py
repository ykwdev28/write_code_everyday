class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        carry = 0
        digits = []

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            total = digit_a + digit_b + carry

            digit = total % 2
            carry = total // 2

            digits.insert(0, digit)

            i -= 1
            j -= 1

        if carry:
            digits.insert(0, carry)

        return ''.join(map(str, digits))