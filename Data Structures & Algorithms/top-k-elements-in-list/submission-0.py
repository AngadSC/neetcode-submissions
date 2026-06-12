class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num,0) + 1

        descending_dict = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}

        first_k_keys = list(descending_dict)[:k]
        return first_k_keys
        