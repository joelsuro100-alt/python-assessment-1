DIGIT_MAP = {  # we will make a dictionary for converting to decimal
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13,
    'E': 14, 'F': 15
}

# we will use this string to convert back from decimal to the base
DIGITS_STR = "0123456789ABCDEF"


def get_decimal_value(input_num_str, base):
    # helper function to convert a single number string to decimal (logic from question 1)
    if len(input_num_str) == 0:
        raise ValueError('no number inserted')

    allowed = list(DIGIT_MAP.keys())[:base]  # allowed characters for the given base

    ans = 0
    power = 1

    # we go over the string from the back to the beginning
    for i in range(len(input_num_str) - 1, -1, -1):
        char = input_num_str[i]
        if char not in allowed:  # checks for illegal chars in this base
            raise ValueError('invalid character inserted in current base')

        digit = DIGIT_MAP[char]
        ans += digit * power
        power *= base

    return ans


def sum_two_numbers_in_base(num1_str, num2_str, base):
    num1_str = num1_str.replace(" ", "").upper()  # cleaning the first number
    num2_str = num2_str.replace(" ", "").upper()  # cleaning the second number

    if base < 2 or base > 16:  # checks if the base is valid
        raise ValueError('invalid base')

    # step 1: convert both numbers to decimal using our helper logic
    dec1 = get_decimal_value(num1_str, base)
    dec2 = get_decimal_value(num2_str, base)

    # step 2: sum them up in decimal
    total_decimal = dec1 + dec2

    # step 3: convert the result back to the requested base (logic from question 2)
    if total_decimal == 0:
        print("0")
        return

    result_digits = []  # we set the list for the result digits

    temp_num = total_decimal
    while temp_num > 0:  # we want to divide as long as we dont get a 0
        remainder = temp_num % base
        result_digits.append(DIGITS_STR[remainder])  # add the char from our string
        temp_num = temp_num // base

    final_result = "".join(result_digits[::-1])  # reverse and join
    print(final_result)


try:
    # input for the two numbers and the base
    number1 = input("Enter the first number: ").replace(" ", "")
    number2 = input("Enter the second number: ").replace(" ", "")
    base_input = input("Enter the base of the numbers: ").replace(" ", "")

    base_int = int(base_input)  # we try to convert base input to int first
except:
    print("invalid input or base")  # catches non-integer inputs for base
else:
    # calls the main function
    try:
        sum_two_numbers_in_base(number1, number2, base_int)
    except ValueError as e:
        print(e)  # prints the specific error message we raised