# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


# [TODO]: fix the function
def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = time_str.split(":")
    int_list = [int(number) for number in list_of_nums]
    return sum(int_list)



def sum_current_time_remove(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    list_of_nums = time_str.split(":")
    list_of_nums = [numbers_string.replace('0','',1) for numbers_string in list_of_nums]
    seperated_nums = []
    for values in list_of_nums:
        for digit in values:
            seperated_nums.append(digit)
    int_list = [int(number) for number in seperated_nums]
    return sum(int_list)
