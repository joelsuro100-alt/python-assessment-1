#will use a dictionary as str cuz thats the output and we can take the index in the str for 10-16
DIGITS = "0123456789ABCDEF"

def decimal_to_base(num, to_base):
    num = num.replace(" ", "")
    if to_base < 2 or to_base > 16:  #check the base that we want to convert to
        raise ValueError("invalid base to convert to")
    if num == 0:  #0 should stay 0 at all times
        print("0")
        return
    if num < 0:  #check that there is no negative num
        raise ValueError("negative numbers not allowed")

    digits = []  # we set the list for the numbers to insert and take backwards

    while num > 0:  #we want to divide as long as we dont get a 0
        remainder = num % to_base  #we take only the remainder of division
        digits.append(DIGITS[remainder])  #add the value from the dictionary
        num = num // to_base  #continue to divide

    result = "".join(digits[::-1])  #reverse the list and put it in a string
    print(result)

try:
    num = input("insert a number in a decimal base that you want to conver its base: ").replace(" ", "")  #first input = num in decima;
    to_base = input("insert a base you want to convert the number to: ").replace(" ", "")  #second input base to convert to
except:  #if its not a number
    raise ValueError("not a valid base")
else:
    decimal_to_base(num, to_base)