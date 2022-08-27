# 03 - Find repeat numbers in an array

## Question 1
> In an array with length of n, all numbers are within the range or 0 to n-1. Some numbers in the array are repeated however we don't know how many numbers are repeated, or how many times each number repeats. Please find any repeated number in the array. For example, if there is an array with length of 7 such as [2,3,1,0,2,5,3], the output repeated number should be 2 or 3.

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

## Question 2

> In an array with length of n+1, all numbers are within the range of 1 to n. Therefore there is at least one repeated number in it. Please find any repeated number in it, but we can't change the input array. For example, if there is an array with length of 8 such as [2,3,5,4,3,2,6,7], the output repeated number should be 2 or 3.

### Solution
This solution uses binary search. The function `count_range` is called O(logn) times for an array with length of n, and in each call it needs time of O(n). Therefore the total time complexity is O(nlogn). Since no new array is created, the space complexity is O(1).
```python
def find_repeat_number(nums: list) -> int:
    """Find any repeat number in the given list

    :param list nums: the given list with length of n+1 and range of [1,n+1]
    :raises ValueError: array should not be empty
    :raises ValueError: number should be within the range of 1 to n
    :return int: any repeat number
    """
    if len(nums) == 0:
        raise ValueError("Array should not be empty.")
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] > len(nums) - 1:
            raise ValueError("Number should be within the range of 1 to n.")

    start = 1
    end = len(nums) - 1
    while start <= end:
        mid = (end - start) // 2 + start
        count = count_range(nums, start, mid)
        if start == end:
            if count > 1:
                return start
        if count > mid - start + 1:
            end = mid
        else:
            start = mid + 1


def count_range(nums: list, start: int, end: int) -> int:
    """Count how many numbers in the list are within the given range

    :param list nums: a list
    :param int start: start of the range
    :param int end: end of the range
    :return int: count of numbers within the range
    """
    count = 0
    for i in range(len(nums)):
        if start <= nums[i] <= end:
            count += 1
    return count
```
