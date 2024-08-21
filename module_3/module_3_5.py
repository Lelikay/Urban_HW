def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    # if '0' in str_number:
    #     result = 0
    #     return result
    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(18380))