class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        word_to_pattern = {}
        pattern_to_word = {}

        words = s.split()

        if len(words) != len(pattern):
            return False

        n = len(words)

        for i in range(n):
            if words[i] not in word_to_pattern and pattern[i] not in pattern_to_word:
                word_to_pattern[words[i]] = pattern[i]
                pattern_to_word[pattern[i]] = words[i]

            else:
                if words[i] in word_to_pattern and word_to_pattern[words[i]] != pattern[i] or pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != words[i]:
                    return False
        return True
