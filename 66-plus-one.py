#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (41.53%)
# Likes:    373
# Dislikes: 0
# Total Accepted:    95.1K
# Total Submissions: 227K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 2019-11-25 11:32 - 11:51 97.32 %
# 边界点：进一位的处理，进一位之后已经到头了的处理
# 延伸：这里因为只是加一，所以每次的进一位的数字只会是1，但如果是两个数字相加，就不会是这样了，就要考虑相加之后，这时候大概是应该取商
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)

        if length == 0:
            return [1]
        
        end = length - 1
        sum = 1      

        while sum > 0 and end >= 0:
            sum += digits[end]
            if sum < 10:
                digits[end] = sum
                sum = 0
            else:
                digits[end] = sum - 10
                end -= 1
                sum = 1

        if sum > 0:
            digits.insert(0, sum)
        return digits
# @lc code=end

