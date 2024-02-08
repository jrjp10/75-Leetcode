class Solution(object):
    def lengthOfLongestSubstring(self, s):
        end = 0
        start = 0
        max_len = 0
        char_set = set()
        
        while start < len(s):
            if s[start] not in char_set:
                char_set.add(s[start])
                max_len = max(max_len, len(char_set))
                start += 1
            else:
                end += 1
                start = end
                char_set.clear()
                
        return max_len
    

s= "abcabcbb"
print(Solution().lengthOfLongestSubstring(s)) # Output: 3