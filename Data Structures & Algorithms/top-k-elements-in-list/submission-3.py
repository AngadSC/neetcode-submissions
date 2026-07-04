class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        answer = []

        for num in nums:
            count[num] = count.get(num,0) + 1 
        
        freq = [[] for i in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)
        
        for sub_arr in reversed(freq):
    
            for value in sub_arr:
                answer.append(value)
                if len(answer) == k:
                    return answer

        return answer

