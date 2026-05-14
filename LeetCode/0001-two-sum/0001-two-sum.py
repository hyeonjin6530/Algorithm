class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for i in range(len(nums)):
            need = target - nums[i]
            
            if need not in dict:
                dict[nums[i]] = i
            else:
                return [i, dict[need]]
