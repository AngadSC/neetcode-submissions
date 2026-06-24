class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts ={}
        left = 0
        best = 0
        max_freq = 0




        for right in range(len(s)):
            char = s[right]
            if char in counts:
                counts[char] +=1
            else:
                counts[char] = 1 

            max_freq = max(max_freq, counts[char])

            window_len = (right - left +1)

            while window_len - max_freq > k:
                counts[s[left]] -=1
                left +=1 
                window_len = (right - left +1)
            
            best = max(window_len, best)
            
    
        return best
            
