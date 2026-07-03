class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        subarray_count = 0

        prefix_sum = {
            0:1 
        } 
        curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            subarray_count += prefix_sum.get(diff,0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum,0) + 1
            
        return subarray_count 

