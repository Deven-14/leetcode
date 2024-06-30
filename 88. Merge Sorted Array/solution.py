class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_nums = nums1[:m]
        
        i, j, k = 0, 0, 0
        while i < m and j < n:

            while i < m and m_nums[i] <= nums2[j]:
                nums1[k] = m_nums[i]
                i = i+1
                k = k+1
            
            if i >= m:
                break

            while j < n and nums2[j] <= m_nums[i]:
                nums1[k] = nums2[j]
                j = j+1
                k = k+1
        
        if i < m:
            nums1[k:] = m_nums[i:]
        elif j < n:
            nums1[k:] = nums2[j:]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        m_nums = nums1[:m]

        i, j, k = 0, 0, 0
        while i < m and m_nums[i] <= nums2[j]:
            i = i+1
            k = k+1
        
        while i < m and j < n:

            while i < m and m_nums[i] <= nums2[j]:
                nums1[k] = m_nums[i]
                i = i+1
                k = k+1
            
            if i >= m:
                break

            while j < n and nums2[j] <= m_nums[i]:
                nums1[k] = nums2[j]
                j = j+1
                k = k+1
        
        if i < m:
            nums1[k:] = m_nums[i:]
        elif j < n:
            nums1[k:] = nums2[j:]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while i >= 0 and j >= 0:
            
            while j >= 0 and nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            
            if j < 0:
                return
            
            while i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        
        if j >= 0:
            nums1[:k+1] = nums2[:j+1]

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        
        if j >= 0:
            nums1[:k+1] = nums2[:j+1]

