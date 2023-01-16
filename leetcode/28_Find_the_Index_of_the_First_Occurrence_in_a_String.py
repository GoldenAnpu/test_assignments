class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        if 1 <= len(haystack) | len(needle) <= 10 ** 4:
            return haystack.lower().find(needle.lower())
        elif len(haystack) < len(needle):
            return -1