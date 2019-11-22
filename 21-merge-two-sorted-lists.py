#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (57.94%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    141.7K
# Total Submissions: 242.8K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2019-11-22 1 11:38 - 12:09
# 归并排序的感觉，长度没有限定，两个指针一直遍历到结尾，终止条件：某一个长度为零（next为None）
# 1. 没考虑到 [] 空链表
# 2. 涉及比较数字大小操作的时候必须用 .val，但是判断是否存在值（None）可以直接用节点
# 3. 弱点：对于链表的指针的引用会不确定
# 4. 参考简洁写法之后运行时间并没有增加（思路一致）

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         i = 0
#         j = 0

#         if not l1:
#             return l2
#         if not l2:
#             return l1

#         i = l1.val
#         j = l2.val
#         if i <= j:
#             result = ListNode(i)
#             l1 = l1.next
#         else:
#             result = ListNode(j)
#             l2 = l2.next
#         p = result

#         while l1 is not None and l2 is not None:
#             i = l1.val
#             j = l2.val
#             if i <= j:
#                 p.next = ListNode(i)
#                 p = p.next
#                 l1 = l1.next
#             else:
#                 p.next = ListNode(j)
#                 p = p.next
#                 l2 = l2.next
        
#         if l1:
#             p.next = l1
#         if l2:
#             p.next = l2
#         return result

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2
        
        n1, n2 = (l1, l2) if l1.val < l2.val else (l2, l1)
        head = n1
        p, n1 = n1, n1.next

        while n1 and n2:
            if n1.val < n2.val:
                p.next = n1
                n1 = n1.next
            else:
                p.next = n2
                n2 = n2.next
            p = p.next
        if n1 or n2:
            p.next = n1 or n2

        return head

# @lc code=end
