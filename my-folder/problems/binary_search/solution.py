class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法
        left, right = 0, len(nums) - 1 # 定義左右的index

        while left <= right:
            mid = (right + left) // 2 # 偶數個數的話，往左取。 ex. [0,1,2,3] 取1
            if nums[mid] < target: # 中間值比目標值小，往後找
                left = mid + 1 # 原本的中間值已經找過不用再找
            elif nums[mid] > target: # 往前找 
                right = mid - 1 
            else: # 若是中間值與目標相等
                return mid
        # 找不到時，left > right，返回-1
        return -1
        