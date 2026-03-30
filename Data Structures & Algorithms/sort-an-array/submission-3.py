class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, mid, r):
            arr1 = arr[l: mid+1]
            arr2 = arr[mid+1: r+1]
            point1 = point2 = 0
            point_arr = l

            while point1<len(arr1) and point2<len(arr2):
                if arr1[point1] <= arr2[point2]:
                    arr[point_arr] = arr1[point1]
                    point_arr+=1
                    point1+=1
                elif arr1[point1] > arr2[point2]:
                    arr[point_arr] = arr2[point2]
                    point_arr+=1
                    point2+=1

            while point1<len(arr1):
                arr[point_arr] = arr1[point1]
                point_arr+=1
                point1+=1
            
            while point2<len(arr2):
                arr[point_arr] = arr2[point2]
                point_arr+=1
                point2+=1

        def mergeSort(arr, l, r):
            if l==r:
                return 
            
            mid = (l+r)//2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)
            merge(arr, l, mid, r)

            return
        
        mergeSort(nums, 0, len(nums)-1)
        return nums