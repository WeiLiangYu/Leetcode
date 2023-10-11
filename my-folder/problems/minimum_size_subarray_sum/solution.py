# 雙指針滑動窗口，O(n)，先計算後標j，再計算前標i
# HINT: i(total) 不會每個後標都重新計算，因為要找比較短的子矩陣，所以比較長的不計算。若計算會超時

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) # 初始化
        if sum(nums) < target:
            return 0
        # HINT
        total = 0
        i = 0

        for j in range(0, len(nums)):
            # 初始化
            total += nums[j] # 當前全部和
            while total >= target:
                Length = j - i + 1
                res = min(res, Length)
                total -= nums[i]               
                i += 1
        return res
        