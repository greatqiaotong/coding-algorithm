# Method 1 - Hash map
# def find_repeat_number(nums):
#     count = {}
#     if len(nums) == 0:
#         raise ValueError("Array should not be empty.")
#     for num in nums:
#         if num < 0 or num > len(nums)-1:
#             raise ValueError("Number should be within the range of 0 to n-1.")
#         if num not in count:
#             count[num] = 1
#         else:
#             count[num] += 1
#             return num

# Method 2 - sorted array
def find_repeat_number(nums):
    if len(nums) == 0:
        raise ValueError("Array should not be empty.")
    for i in range(len(nums)):
        if nums[i] < 0 or nums[i] > len(nums) - 1:
            raise ValueError("Number should be within the range of 0 to n-1.")
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
