class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in nums1[:]:
            if ( i == 0 and len(nums1) > m ):
                nums1.remove(0)
        for i in nums2[:]:
            if ( i == 0 and len(nums2) > n ):
                nums2.remove(0)
        nums1.extend(nums2) 
        nums1.sort()
        

        