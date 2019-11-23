#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# 2019-11-23 10:50
# 想用归并排序但还是不熟练，只能用普通
# 11:21 先打算从前面遍历指针，后来发现可以从后面开始
# 11:35 最终提交。对于
# 12:02 68.19% 终于……通过了……就是各种在末尾的条件没有处理好的感觉。

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1 = nums2
        if n == 0:
            return nums1
        
        i = m - 1
        j = n - 1
        k = i + j + 1

        while k >= 0 and i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
            # print(nums1)
        

# @lc code=end

