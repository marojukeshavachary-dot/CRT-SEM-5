def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    window = nums[:k]
    res = [max(window)]
    for i in range(k, len(nums)):
        window = nums[i-k+1:i+1]
        res.append(max(window))
    return res
            

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))