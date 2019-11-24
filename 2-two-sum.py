#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# 2019-11-24 11:13 2 - 11:26 72.96 %
# 把减的操作挪到判断后面之后 96 %
# 方案二：用字典来存每个数字的下标和它对应的匹配数字
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v_map = {}
        for idx, i in enumerate(nums):
            # print(v_map)
            if i in v_map:
                return [v_map[i], idx]
            else:
                left = target - i
                v_map[left] = idx
        return []

# 方案一，先 sort 然后从小往大选，不对，这样丢了下标了……
# @lc code=end

