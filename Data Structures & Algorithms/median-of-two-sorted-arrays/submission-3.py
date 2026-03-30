class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # keeping nums2 the smaller array
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        # finding correct left_subarray
        total_elements = len(nums1) + len(nums2)

        l2 = 0
        r2 = len(nums2)-1
        mid2 = None
        mid1 = None
        nums1_left = None # rightmost ele of left_subarray of nums1
        nums1_right = None # leftmost ele of right_subarray of nums1
        nums2_left = None # rightmost ele of left_subarray of nums2
        nums2_right = None # leftmost ele of right_subarray of nums2
        while True:
            mid2 = l2 + (r2 - l2)//2

            left_subarray_count2 = mid2+1 #number of elements in left_subarray of nums2
            left_subarray_count1 = total_elements//2 - left_subarray_count2 #number of elements in left_subbary of nums1

            mid1 = left_subarray_count1-1

            # handling edgecases
            nums1_left = nums1[mid1] if mid1>=0 else float('-inf') # no elements of nums1 selected
            nums1_right = nums1[mid1 + 1] if (mid1+1) < len(nums1) else float('inf') # all elements of nums1 selected 
            nums2_left = nums2[mid2] if mid2>=0 else float('-inf') # no elements of nums2 selected 
            nums2_right = nums2[mid2 + 1] if (mid2+1) < len(nums2) else float('inf') # all elements of nums2 selected

            print(f'({nums1_left}, {nums1_right}), ({nums2_left}, {nums2_right})')
            # if selected left_subarray is valid
            if nums1_left <= nums2_right and nums2_left <= nums1_right: 
                break

            elif nums2_left > nums1_right:
                r2 = mid2 - 1
            else:
                l2 = mid2 + 1

        #finding median
        answer = None
        if total_elements%2 == 1:
            answer = min(nums1_right, nums2_right)
        
        else:
            answer = (max(nums1_left, nums2_left) + min(nums1_right, nums2_right))/2
            
        return answer