class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        if not words:
            return ""
        
        prefix = words[0]

        for i in range(len(prefix)):
            current_char = prefix[i]

            for word in words:
                if len(word) <= i or word[i] != current_char:
                    return prefix[:i]
        
        return prefix

