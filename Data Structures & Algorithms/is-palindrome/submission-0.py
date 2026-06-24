class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(filter(str.isalnum, s))
        
        left = 0
        right = len(text) -1 

        while left < right:
            if text[left].lower() == text[right].lower():
                left += 1
                right -=1
            else:
                return False
        
        return True 
                
            
        
        