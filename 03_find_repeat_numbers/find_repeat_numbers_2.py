# Binary search
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
