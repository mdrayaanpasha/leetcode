class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        Words=s.split()
        Words.reverse()
        return " ".join(Words)