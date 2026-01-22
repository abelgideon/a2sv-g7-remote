class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringForm = str(x)

        return str(x) == stringForm[::-1]