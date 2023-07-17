class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(" ")

        last_word = words[-1]

        return len(last_word)
