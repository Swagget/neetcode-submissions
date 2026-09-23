class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m + j and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                print(nums1)
                i += 1
                for temp in range(m+n-1, i-1, -1):
                    nums1[temp] = nums1[temp-1]
                nums1[i-1] = nums2[j]
                j += 1
        if j < n:
            for temp in range(j, n):
                nums1[i] = nums2[temp]
                i += 1
