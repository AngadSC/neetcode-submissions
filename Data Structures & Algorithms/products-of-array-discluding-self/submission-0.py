class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        
        for i in range(len(nums)):
            count = 1 
            
            for num in nums[i+1:]:
                count *= num
            for num in nums[0:i]:
                count *= num 
            
            output.append(count)
        
        return output 
        

            
                
