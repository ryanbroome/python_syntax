def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """
    count = 0
    for num in nums:
        if type(num) is int:
            count += num
        else :return print('input type must be integers to use sum_nums, try again with integers')

    return count
      
    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.


    # YOUR CODE HERE



print("sum_nums returned", sum_nums([1, 2, 3, 4]))
