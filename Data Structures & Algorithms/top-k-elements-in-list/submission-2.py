class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        answer = []

        for num in nums:
            count[num] = count.get(num,0) + 1 
        
        sorted_data_desc = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

        for key in list(sorted_data_desc.keys())[:k]:
            answer.append(key)
        
        return answer 

