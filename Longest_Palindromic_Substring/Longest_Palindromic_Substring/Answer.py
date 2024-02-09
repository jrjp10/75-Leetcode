class Solutions:
    def longest_palindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the palindrome substring

        result = ''
        for i in range(len(s)):
            # Consider each character as the center of a palindrome.
            odd = expand_around_center(i, i)
            even = expand_around_center(i, i + 1)
            # Update result if a longer palindrome is found
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result

# Test the function
print(Solutions().longest_palindrome("abdbca"))  # Output: "bdb"
print(Solutions().longest_palindrome("cbbd"))     # Output:
    