# 03 - Find repeat numbers in an array

## Question 1
> In an array with length of n, all numbers are within the range or 0 to n-1. Some numbers in the array are repeated however we don't know how many numbers are repeated, or how many times each number repeats. Please find any repeated number in the array. For example, if there is an array with length of 7 such as [2,3,1,0,2,5,3], the output repeat number should be 2 or 3.

### Solution 1
It uses hash map. Time complexity is O(n) and space complexity is O(n) as a hash map is created.
```python
def find_repeat_number(nums):
    count = {}
    if len(nums) == 0:
        raise ValueError("Array should not be empty.")
    for num in nums:
        if num < 0 or num > len(nums)-1:
            raise ValueError("Array should be within the range of 0 to n-1")
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
            return num
```
### Solution 2
Because the array length is n and all number within it are in the range of 0 to n-1, which means in the sorted array, the number i should array at index i if there is no repeated number. Because there are repeated number, there would be multiple numbers appearing at the same index, or for some index there would be no numbers.

This method has time complexity of O(n) and space complexity of O(1).
```python
def find_repeat_number(nums):
    if len(nums) == 0:
        raise ValueError("Array should not be empty.")
    for i in range(len(nums)):
        if nums[i] < 0 or nums[i] > len(nums)-1:
            raise ValueError("Array should be within the range of 0 to n-1")
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
```