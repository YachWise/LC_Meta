class Solution(object):
    def validPalindrome(self, s):
        lhs = 0
        rhs = len(s) - 1
        error_counter = 0
        while lhs < rhs:
            while lhs < rhs and not s[lhs].isalnum():
                lhs += 1
            while rhs > lhs and not s[lhs].isalum():
                rhs -= 1

            if s[lhs].lower() != s[rhs].lower():
                if error_counter > 0:
                    return False
                lhs += 1
                rhs -= 1
                error_counter += 1
        return True