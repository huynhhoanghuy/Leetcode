class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i,value in enumerate(nums):
            if value not in dict_nums:
                dict_nums[value] = i
            
            if dict_nums.get((target - value),-1) != -1:
                j = dict_nums[target-value]
                if i < j:
                    return [i,j]
                elif i> j:
                    return [j,i]

#get in dictionary has O(1)
#Runtime: 121 ms faster than 42.53% of Python3 online submissions for Two Sum
#Memory: 15.2 MB less than 50.50% of Python3 online submissions for Two Sum.

