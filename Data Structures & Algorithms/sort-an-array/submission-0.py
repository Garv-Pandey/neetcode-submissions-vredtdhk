class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, mid, r):
            l_arr = arr[l: mid+1]
            r_arr = arr[mid+1: r+1]

            i = l
            l_point = 0
            r_point = 0
            while l_point < len(l_arr) and r_point < len(r_arr):
                if l_arr[l_point]<=r_arr[r_point]:
                    arr[i]=l_arr[l_point]
                    l_point+=1

                elif l_arr[l_point]>r_arr[r_point]:
                    arr[i]=r_arr[r_point]
                    r_point+=1
                
                i+=1

            while l_point < len(l_arr):
                arr[i] = l_arr[l_point]
                i+=1
                l_point+=1

            while r_point < len(r_arr):
                arr[i] = r_arr[r_point]
                i+=1
                r_point+=1
        
        
        def mergeSort(arr, l, r):
            if l==r:
                return 

            mid = (r+l)//2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid+1, r)
            merge(arr, l, mid, r)
            return


        mergeSort(nums, 0, len(nums)-1)

        return nums
