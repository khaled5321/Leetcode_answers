class Solution:
    def characterReplacement(self, s: str, k: int) -> int:    
        length = 0
        dic = {}
        l = 0
        for r in range(len(s)):
            if s[r] not in dic:
                dic[s[r]] = 1
            else:
                dic[s[r]] += 1 

            window_size = (r - l + 1)
            maxFrequent = dic[max(dic, key=dic.get)]

            if (window_size - maxFrequent) <= k:
                length = max(length, window_size)
            else:
                dic[s[l]] -= 1
                l = l + 1
                
        return length
