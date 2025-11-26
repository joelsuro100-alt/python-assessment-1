DIGIT_MAP = { #we will make a dictionary on the side for all the bases as suggested by my classmate 'Gonen'
    '0': 0,  '1': 1,  '2': 2,  '3': 3,
    '4': 4,  '5': 5,  '6': 6,  '7': 7,
    '8': 8,  '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13,
    'E': 14, 'F': 15
}

def base_to_decimal(input_num_str, base):
    input_num_str = input_num_str.replace(" ", "").upper()  #we removed all the empty unnecessary spaces

    if base < 2 or base > 16:  #cheks if the base is valid
        raise ValueError('invalid base')

    if '-' in input_num_str:  #checks if the user entered a negative
        raise ValueError('negative sign is not allowed')

    if len(input_num_str) == 0:  #checks if after removal of spaces if its empty
        raise ValueError('no number inserted')

    #we take only the keys allowed for this base (base 2 = '0','1')
    allowed = list(DIGIT_MAP.keys())[:base]  #allowed characters for the given base

    #we check if each char is legal in current base
    for char in input_num_str:  #we check for illegal chars
        if char not in allowed:
            raise ValueError('invalid character inserted in current base')

    ans = 0  #were setting answer
    power = 1  #we are setting the power of the number to 1 cuz num power 0 =1 in beginning

    #we go over the string from the back to the beginning
    for i in range(len(input_num_str) - 1, -1, -1):
        char = input_num_str[i]  #current character from right to left
        digit = DIGIT_MAP[char]  #convert char to number using our dictionary

        if digit >= base:  #checks to see if added a num bigger than base = error
            raise ValueError('digit too large for base')

        ans += digit * power  #the normal conversion formula
        power *= base  #increase the place-value power by multiplying by base

    print(ans)

try:
    str_number = input("Enter a number to move to decimal base: ").replace(" ", "")
    base = input("enter the number current base: ").replace(" ", "")
except:
    print("invalid base")  #checks if base valid
else:
    base_to_decimal(str_number, base)  #calls the function and prints the outcome



