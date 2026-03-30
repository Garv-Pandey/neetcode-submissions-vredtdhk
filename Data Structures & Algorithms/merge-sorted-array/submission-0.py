class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_point = m-1
        num2_point = n-1
        update_point = m+n-1

        while num1_point > -1 and num2_point > -1:
            if nums1[num1_point] >= nums2[num2_point]:
                nums1[update_point] = nums1[num1_point]
                num1_point-=1

            else:
                nums1[update_point] = nums2[num2_point]
                num2_point-=1

            update_point -= 1
            print(num1_point, num2_point)

        while num1_point > -1:
            nums1[update_point] = nums1[num1_point]
            num1_point-=1
            update_point-=1

        while num2_point > -1:
            nums1[update_point] = nums2[num2_point]
            num2_point-=1
            update_point-=1

        
        