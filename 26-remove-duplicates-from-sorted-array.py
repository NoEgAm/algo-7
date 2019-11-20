# First Try 	132 ms	16 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        store = {}
        idx = 0
        while idx < len(nums):
            num = nums[idx]
            if store.get(num):
                del nums[idx]
            else:
                store[num] = True
                idx = idx + 1

        return len(nums)

# 看了答案之后的 	108 ms	15.2 MB

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        jdx = 1
        while idx < len(nums) and jdx < len(nums):
            if nums[idx] != nums[jdx]:
                idx = idx + 1
                nums[idx] = nums[jdx]
            jdx = jdx + 1

        return len(nums[:idx+1])
        
# 最开始没有注意到在删除的过程里面长度会变化
# 参考解法里面，需要注意最终返回的长度是根据 i 指针来定的。
