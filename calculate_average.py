numbers = [1, 2, 3]


def find_average(nums):
    nums_sum = 0
    for x in nums:
        nums_sum += x
    return nums_sum / len(nums)
