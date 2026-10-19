class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Pointers for front and back letters, converging
        front, back = None, None
        # String containing only alphanumerics in s
        lnumstring = ""
        # Append to the new string, ignoring non-alphanumerics
        for i in range(len(s)):
            if s[i].isalnum():
                lnumstring += s[i]
        # Make lnumstring lowercase so that case doesn't matter
        lnumstring = lnumstring.lower()
        # If s had no valid lnums
        if not lnumstring:
            return True
        # Compare the front and back letters, converging towards middle
        for i in range(int(len(lnumstring)/2) + 1):
            front = lnumstring[i]
            back = lnumstring[len(lnumstring) - 1 - i]
            # Return false is they don't match
            if front != back:
                return False
        # Return true if all the letters matched
        return True