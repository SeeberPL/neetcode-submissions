class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        seen = set()
        for num in nums:
            if num in seen:
                result = True
            else:
                seen.add(num)
        return result