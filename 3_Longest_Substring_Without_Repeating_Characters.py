class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        dic = {s[0]:0,}
        length = 1
        l = 0

        for r in range(1, len(s)):
            if s[r] not in dic:
                length = max(length, r - l + 1)
            else:
                if dic[s[r]] < l:
                    length = max(length, r - l + 1)
                else:
                    l = dic[s[r]] + 1

            dic[s[r]] = r

        return length
