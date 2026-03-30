class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        update_point = m+n-1
        point1=m-1
        point2=n-1

        while point1 >=0 and point2>=0:
            if nums1[point1] >= nums2[point2]:
                nums1[update_point] = nums1[point1]
                update_point-=1
                point1-=1
            elif nums1[point1] < nums2[point2]:
                nums1[update_point] = nums2[point2]
                update_point-=1
                point2-=1

        while point1 >=0:
            nums1[update_point] = nums1[point1]
            update_point-=1
            point1-=1
            
        while point2 >=0:
            nums1[update_point] = nums2[point2]
            update_point-=1
            point2-=1