class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(l, r):
            p = nums[r] # choosing random is better
            i = l
            for j in range(l, r):
                if nums[j] > p: # greater ones to the left
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[r] = nums[r], nums[i]
            return i

        def kth_smallest_element(l, r, k): # k [1, n]
            i = partition(l, r)

            if i == (k-1):
                return nums[i]
            
            if i < (k-1):
                return kth_smallest_element(i+1, r, k)
            
            return kth_smallest_element(l, i-1, k)
        
        # we are finding the kth smallest element along with partitioning
        # if you want to only find the kth smallest without partitioning, then use quick_select
        n = len(nums)

        if n < 2:
            return

        mid = n // 2
        mid_ele = kth_smallest_element(0, n-1, mid)

        m = n|1 # if n is even return n+1
        def virtual_index(i):
            return (2 * i + 1) % m
        
        # Dutch National Flag Problem # 3 pointer # sort 0s, 1s, 2s
        low, mid, high = 0, 0, n-1
        while mid <= high:
            v_mid = virtual_index(mid)
            if nums[v_mid] > mid_ele:
                v_low = virtual_index(low)
                nums[v_low], nums[v_mid] = nums[v_mid], nums[v_low]
                low += 1
                mid += 1
            elif nums[v_mid] < mid_ele:
                v_high = virtual_index(high)
                nums[v_high], nums[v_mid] = nums[v_mid], nums[v_high]
                high -= 1
            else: # == mid_ele
                mid += 1


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        nums.sort()
        mid = n // 2 + (0 if n % 2 == 0 else 1)
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]