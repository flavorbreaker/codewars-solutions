numbers = [1, 2, 3]                 # creates a list of integers


def find_average(nums):             # creates the function find_average and passes the nums parameter
    nums_sum = 0                    # creates a variable to hold the sum of nums, initializing to 0
    for x in nums:                  # loops over every item in nums
        nums_sum += x               # adds each item in nums to nums_sum
    return nums_sum / len(nums)     # returns nums_sum divided by the number of indices in nums
