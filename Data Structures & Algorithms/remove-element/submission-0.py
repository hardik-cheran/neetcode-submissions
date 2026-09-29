class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for _ in nums:
            if _ != val:
                nums[k] = _
                k+=1
        return k

