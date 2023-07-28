class Solution:
    def countSubstrings(self, s: str) -> int:
        number = 0

        for i in range(0, len(s)):
            for j in range(1, len(s)+1):
                current_string = s[i:j]
                if current_string and current_string == current_string[::-1]:
                    number += 1
                  
        return number
