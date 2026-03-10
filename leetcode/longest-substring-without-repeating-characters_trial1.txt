class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        L = 0
        count = defaultdict(int)

        for R in range(len(s)):
            count[s[R]] += 1

            while count[s[R]] > 1:
                count[s[L]] -= 1
                L += 1
            
            longest = max(longest, R - L + 1)
        
        return longest