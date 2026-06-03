class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {} 
        for num in nums:
            if num in counts:
                if counts[num] == 1:
                    return True
            else:
                counts[num] =1
        
        return False