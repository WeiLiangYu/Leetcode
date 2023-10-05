class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指針法，不刪除元素，將陣列覆蓋
        slow, fast = 0, 0
        for i in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow