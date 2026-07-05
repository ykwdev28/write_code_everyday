class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs[0])):
            c = strs[0][i]

            for s in strs[1:]:
                if i == len(s) or s[i] != c:
                    return strs[0][:i]

        return strs[0]