class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        prefix = ''
        new_slice = strs[1:]
        main_word = [i for i in strs[0]]
        if len(strs) == 1 or strs[0] == "":
            return strs[0]
        while True:
            prefix += main_word.pop(0)
            for word in new_slice:
                if word.startswith(prefix):
                    continue
                else:
                    prefix = prefix[:-1]
                    return prefix
            if not main_word:
                return prefix
