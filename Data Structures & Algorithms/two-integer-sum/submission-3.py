class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {} 

        for i, num in enumerate(nums):
            need = target - num 

            if need in count:
                return[count[need],i]
            else:
                count[num] = count.get(num,0) + i
        
        

            

        