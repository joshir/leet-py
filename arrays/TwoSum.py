def twoSum(nums, target):
    m = {}
    for i, num in enumerate(nums):
        diff = target - nums
        if diff in m:
            return [m[diff], i]
        else:
            m[num] = i


