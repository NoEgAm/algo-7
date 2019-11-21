#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Easy (39.15%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    79.2K
# Total Submissions: 201.2K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 说明:
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
# 
# 
#

# 2019-11-20 1
# 最开始尝试了题目说的移位+多次的方式，时间复杂度是 O(k*n) 导致在跑过大的数组时候会超过时间限制。
# 之后尝试每次移位k间隔，参考答案之后发现自己的漏洞有：
# 1. 如果提前处理 k 对长度取模，可以减少很多时间，直接排除了 k = 0 的耗时
# 2. 如何管理指针，比如处理移位一轮之后回到起点的情况，通过外层循环设置每次起始位置，并通过两指针相等来判断是否回到起始位置
# 3. 在写的过程里面会漏掉很多 case 导致提交后A通过B通不过，改一改之后又反过来，以后可以试试先想想各种边界条件

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        idx = 0
        start = 0
        times = 0

        k = k % lens

        if k == 0:
            return nums

        while times < lens:
            idx = start
            tmp = nums[idx]

            to_idx = (idx + k) % lens
            to_tmp = nums[to_idx]
            nums[to_idx] = tmp
            idx = to_idx
            tmp = to_tmp
            times = times + 1
            
            while start != idx:
                to_idx = (idx + k) % lens
                to_tmp = nums[to_idx]
                nums[to_idx] = tmp
                idx = to_idx
                tmp = to_tmp
                times = times + 1

            start = start + 1
        
# @lc code=end
