class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum34_counts = defaultdict(int)
        for num3 in nums3:
            for num4 in nums4:
                sum34_counts[num3 + num4] += 1
        
        sum4_count = 0
        for i, num1 in enumerate(nums1):
            for j, num2 in enumerate(nums2):
                sum2 = num1 + num2
                if -sum2 in sum34_counts:
                    sum4_count += sum34_counts[-sum2]
        
        return sum4_count


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum34_counts = defaultdict(int)
        for num3 in nums3:
            for num4 in nums4:
                sum34_counts[num3 + num4] += 1
        
        sum12_counts = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                sum12_counts[num1 + num2] += 1
        
        sum4_count = 0
        for sum12 in sum12_counts.keys():
            if -sum12 in sum34_counts:
                sum4_count += sum12_counts[sum12] * sum34_counts[-sum12]
            
        return sum4_count


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1, nums2, nums3, nums4 = Counter(nums1), Counter(nums2), Counter(nums3), Counter(nums4)

        sum34_counts = defaultdict(int)
        for num3 in nums3:
            for num4 in nums4:
                sum34_counts[num3 + num4] += nums3[num3] * nums4[num4]
        
        sum4_count = 0
        for num1 in nums1:
            for num2 in nums2:
                sum12 = num1 + num2
                if -sum12 in sum34_counts:
                    sum4_count += nums1[num1] * nums2[num2] * sum34_counts[-sum12]
        
        return sum4_count