class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        count1 = dict(sorted(count.items(), key = lambda items : items[1], reverse = True))
        first_key = next(iter(count1))
        return first_key
        