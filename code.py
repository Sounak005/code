
class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(nums):
      if target - num in d:
        return [d[target - num], i]
      d[num] = i     

x=Solution.twoSum(6,[1,2,4],5)
print(x)