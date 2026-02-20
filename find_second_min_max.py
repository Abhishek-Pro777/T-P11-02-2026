def find_second_maximum(nums):
    if len(nums) < 2:
        return None  
    max1 = max2 = float('-inf')
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num < max1: # Ensures distinct values for max1 and max2
            max2 = num
    return max2 if max2 != float('-inf') else None # Check if a second max was found
