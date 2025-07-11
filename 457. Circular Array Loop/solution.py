class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def has_cycle(i):
            if nums[i] == 0:
                return False
                        
            slow = i
            fast = (i + nums[i] + n) % n
            if slow == fast:
                return False
            
            while slow != fast and nums[slow] != 0 and nums[fast] != 0:
                slow = (slow + nums[slow] + n) % n
                fast = (fast + nums[fast] + n) % n
                fast = (fast + nums[fast] + n) % n
            
            if nums[slow] == 0 or nums[fast] == 0:
                return False

            start = slow
            forward, backward = nums[start] > 0, nums[start] < 0
            t = nums[start]
            nums[start] = 0
            start = (start + t + n) % n

            if start == slow:
                return False

            while start != slow:
                forward |= nums[start] > 0
                backward |= nums[start] < 0
                t = nums[start]
                nums[start] = 0
                start = (start + t + n) % n
            
            return forward ^ backward
        
        for i in range(len(nums)):
            if has_cycle(i):
                return True
        
        return False


# ! slower

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def has_cycle(i):
            if nums[i] == 0:
                return False
                        
            slow = i
            direction = nums[i] > 0
            fast = (i + nums[i]) % n
            if slow == fast or (nums[fast] > 0) != direction:
                return False
            

            while slow != fast:
                slow = (slow + nums[slow]) % n
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break

                fast = (fast + nums[fast]) % n
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break

                fast = (fast + nums[fast]) % n
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
            
            if slow != fast or nums[slow] == 0 or nums[fast] == 0 or (nums[slow] > 0) != direction and (nums[fast] > 0) != direction:
                return False

            start = slow
            t = nums[start]
            nums[start] = 0
            start = (start + t) % n

            if start == slow:
                return False

            while start != slow:
                t = nums[start]
                nums[start] = 0
                start = (start + t) % n
            
            return True
        
        for i in range(len(nums)):
            if has_cycle(i):
                return True
        
        return False


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def has_cycle(i):
            if nums[i] == 0:
                return False
                        
            slow = i
            direction = nums[i] > 0
            fast = (i + nums[i]) % n
            if slow == fast or (nums[fast] > 0) != direction:
                return False

            while slow != fast:
                slow = (slow + nums[slow]) % n
                if (nums[slow] > 0) != direction:
                    break

                fast = (fast + nums[fast]) % n
                if (nums[fast] > 0) != direction:
                    break

                fast = (fast + nums[fast]) % n
                if (nums[fast] > 0) != direction:
                    break
                
            else:
                fast = (fast + nums[fast]) % n
                return slow != fast # self loop
            
            start = i
            while (nums[start] > 0) != direction:
                t = nums[start]
                nums[start] = 0
                start = (start + t) % n
            
            return False
                    
        for i in range(len(nums)):
            if has_cycle(i):
                return True
        
        return False


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def has_cycle(i):
            if nums[i] == 0:
                return False
                        
            slow = i
            direction = nums[i] > 0
            fast = (i + nums[i]) % n
            if slow == fast or (nums[fast] > 0) != direction:
                return False

            while slow != fast:
                slow = (slow + nums[slow]) % n
                if (nums[slow] > 0) != direction:
                    break

                fast = (fast + nums[fast]) % n
                if (nums[fast] > 0) != direction:
                    break

                fast = (fast + nums[fast]) % n
                if (nums[fast] > 0) != direction:
                    break
                
            else:
                fast = (fast + nums[fast]) % n
                if slow != fast: # self loop
                    return True
            
            start = i
            while (nums[start] > 0) != direction:
                t = nums[start]
                nums[start] = 0
                start = (start + t) % n
            
            return False
                    
        for i in range(len(nums)):
            if has_cycle(i):
                return True
        
        return False


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_idx(i):
            return (i + nums[i]) % n

        def has_cycle(i):    
            slow = i
            direction = nums[i] > 0
            fast = next_idx(i)
            if slow == fast or (nums[fast] > 0) != direction:
                return False

            while slow != fast:
                slow = next_idx(slow)
                fast2 = next_idx(fast)
                fast = next_idx(fast2)
                if (nums[slow] > 0) != direction or (nums[fast2] > 0) != direction or (nums[fast] > 0) != direction:
                    break
                
            else:
                fast = next_idx(fast)
                if slow != fast: # self loop
                    return True
            
            start = i
            while (nums[start] > 0) != direction:
                t = nums[start]
                nums[start] = 0
                start = next_idx(start)
            
            return False
                    
        for i in range(len(nums)):
            if nums[i] != 0 and has_cycle(i):
                return True
        
        return False


# * issue was in the skipping logic `while nums[start] != 0 and (nums[start] > 0) == direction:`

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_idx(i):
            return (i + nums[i]) % n

        def has_cycle(i):    
            slow = i
            direction = nums[i] > 0
            fast = next_idx(i)
            if slow == fast or (nums[fast] > 0) != direction:
                return False

            while slow != fast:
                slow = next_idx(slow)
                fast2 = next_idx(fast)
                fast = next_idx(fast2)
                if (nums[slow] > 0) != direction or (nums[fast2] > 0) != direction or (nums[fast] > 0) != direction:
                    break
                
            else:
                fast = next_idx(fast)
                if slow != fast: # self loop
                    return True
            
            start = i
            while nums[start] != 0 and (nums[start] > 0) == direction:
                next = next_idx(start)
                nums[start] = 0
                start = next
            
            return False
                    
        for i in range(len(nums)):
            if nums[i] != 0 and has_cycle(i):
                return True
        
        return False