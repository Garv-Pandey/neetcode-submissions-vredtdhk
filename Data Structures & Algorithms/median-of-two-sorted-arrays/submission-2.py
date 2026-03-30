class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_ele = len(nums1) + len(nums2)
        half_count = total_ele//2
        
        # keeping nums1 smaller 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1


        # finding the middle element of combined array from both the arrays
        l1 = 0
        r1 = (len(nums1)-1) #-1 to make in 0 based index

        while True:
            mid1 = l1 + (r1 - l1)//2

            # mid2 + 1 = half - (mid1 + 1)
            # => mid2 = half - mid1 - 2
            mid2 = half_count - mid1 -2 

            mid1_ele = nums1[mid1] if mid1>=0 else float('-inf')
            mid2_ele = nums2[mid2] if mid2>=0 else float('-inf')

            mid1_next = nums1[mid1+1] if mid1+1<len(nums1) else float('inf')
            mid2_next = nums2[mid2+1] if mid2+1<len(nums2) else float('inf')

            if mid1_ele > mid2_next:
                r1 = mid1-1

            elif mid2_ele > mid1_next:
                l1 = mid1+1

            else:
                if total_ele%2 == 1:
                    return min(mid1_next, mid2_next)
                
                else:
                    return (max(mid1_ele, mid2_ele) + min(mid1_next, mid2_next))/2