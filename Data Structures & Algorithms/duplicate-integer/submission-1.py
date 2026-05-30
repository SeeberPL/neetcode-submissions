class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        seen = set(nums)
        if len(nums) > len(seen):
            result = True
        return result