class Solution:
    def repeated_sSubstring_pattern(self, s: str) -> bool:
        for index in range(1, len(s)):
            no_of_occurrences = len(s) // index
            if s[0:index] * no_of_occurrences == s:
                return True
        return False
