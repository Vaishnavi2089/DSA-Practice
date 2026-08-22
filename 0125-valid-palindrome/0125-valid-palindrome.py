class Solution:
    def helper(self,s,left,right):
        if left>=right:
            return True
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        return self.helper(s,left+1,right-1)
    def isPalindrome(self, s: str) -> bool:
        return self.helper(s,0,len(s)-1)

        