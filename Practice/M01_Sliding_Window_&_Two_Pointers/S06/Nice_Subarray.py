'''






class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(goal: int) -> int:
            if goal < 0:
                return 0 
            left = 0 
            odd_count = 0 
            subarrays = 0 

            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    odd_count += 1 
                while odd_count > goal:
                    if nums[left] % 2 != 0:
                        odd_count -= 1 
                    left += 1
                subarrays += (right - left + 1)
            return subarrays 
        return atMost(k) - atMost(k - 1)
    
nums = [1,1,2,1,1]
k = 3 
print(numberOfSubarrays(nums,k))
'''
def longestNiceSubstring(s: str) -> str:
        if len(s) < 2:
            return ""
        
        unique = set(s)
        for i, ch in enumerate(s):
            if ch.lower() in unique and ch.upper() in unique:
                continue
            
            left_str = longestNiceSubstring(s[:i])
            right_str = longestNiceSubstring(s[i+1:])
            
            return left_str if len(left_str) >= len(right_str) else right_str
            
        return s 
s = "YazaAay"
print(longestNiceSubstring(s))
    