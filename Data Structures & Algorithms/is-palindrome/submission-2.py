import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = "".join(re.findall(r"[A-Za-z0-9]", s)).lower()
        return temp == temp[::-1]