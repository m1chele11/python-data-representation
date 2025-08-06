import re


# 1) 
def recognize_and_convert(number_str):
    try:
        is_negative = number_str.startswith("-")
        clean_number = number_str.lstrip("-")  # Remove '-' temporarily for base detection

        # Recognize the base
        if clean_number.startswith("0b"):
            base, num_type = 2, "Binary"
        elif clean_number.startswith("0o"):
            base, num_type = 8, "Octal"
        elif clean_number.startswith("0x"):
            base, num_type = 16, "Hexadecimal"
        else:
            base, num_type = 10, "Decimal"
        
        # Convert to decimal
        decimal_value = int(clean_number, base)

        # Reapply negative sign if needed
        if is_negative:
            decimal_value = -decimal_value

        # Output converted values
        print(f"Input Type: {num_type}")
        print(f"Decimal: {decimal_value}")
        print(f"Octal: {oct(decimal_value)}")
        print(f"Hexadecimal: {hex(decimal_value)}")
    except ValueError:
        print("Invalid number format!")

# Test function to iterate over list of numbers
def test_recognize_and_convert():
    test_numbers = ["0b1101", "0b101010", "0o777", "0o1234", "42", "789", "0x1A", "0xFF", "0b2",
                    "0o89", "0xGHI", "-0o777", "", "Hello There"]
    print("--- Number Type Recognition & Conversion ---")
    for num in test_numbers:
        print(f"\nTesting: {num}")
        recognize_and_convert(num)

test_recognize_and_convert()


#check if string is valid binary by matching 0s & 1s
def is_valid_binary(number):
    return re.fullmatch(r'[01]+', number) is not None

# 2)

# C)
def binary_subtraction_borrow(bin1, bin2):
    try:
        dec1, dec2 = int(bin1, 2), int(bin2, 2) #convert binary to decimal
        result = dec1 - dec2
        if result < 0:
            print("Subtraction resulted in a negative number.")
        else:
            print(f"Borrow Method Result: {bin(result)[2:]}")
    except ValueError:
        print("Invalid binary input!")

def test_binary_subtraction_borrow():
    print("\n--- Binary Subtraction (Borrow Method) ---")
    test_binary_pairs = [("1011001100001111010101", "0111000101010"),
                         ("00101110101001010", "0101"),
                         ("11100", "100101011"), ("1100", "1010"),
                         ("00101110101001010", "0101.111.1")]
    
    for bin1, bin2 in test_binary_pairs:
        print(f"\nSubtracting {bin2} from {bin1}")
        if is_valid_binary(bin1) and is_valid_binary(bin2):
            binary_subtraction_borrow(bin1, bin2)
        else:
            print("Invalid binary numbers provided!")

test_binary_subtraction_borrow()

# D)

def binary_subtraction_twos_complement(bin1, bin2):
    try:
        max_len = max(len(bin1), len(bin2))
        bin1, bin2 = bin1.zfill(max_len), bin2.zfill(max_len) #zero-pad both binary numbers, ensuring they have the same length.
        
        dec1, dec2 = int(bin1, 2), int(bin2, 2) #conversion then subtraction fo the numbres
        result = dec1 - dec2
        
        if result < 0:
            print("Subtraction resulted in a negative number.")
        else:
            print(f"Two's Complement Result: {bin(result)[2:]}")
    except ValueError:
        print("Invalid binary input!")

def test_binary_subtraction_twos_complement():
    print("\n--- Binary Subtraction (Two's Complement Method) ---")
    test_binary_pairs = [("1011001100001111010101", "0111000101010"),
                         ("00101110101001010", "0101"),
                         ("11100", "100101011"), ("1100", "1010")]
    
    for bin1, bin2 in test_binary_pairs:
        print(f"\nSubtracting {bin2} from {bin1}")
        if is_valid_binary(bin1) and is_valid_binary(bin2):
            binary_subtraction_twos_complement(bin1, bin2)
        else:
            print("Invalid binary numbers provided!")


test_binary_subtraction_twos_complement()


# 3)

#Explanation is in the txt file, some illustration code here:

print("_________ Start of Question 3 __________")

# A)
binary_str = "01011001011001010111001100100001" 
decimal_value = int(binary_str, 2) #go through each bit to find the decimal representation
print(decimal_value)

# B)

def twos_complement_to_decimal(binary_str):
    if binary_str[0] == '0':  # Positive number
        return int(binary_str, 2)
    else:  # Negative number
        return int(binary_str, 2) - (1 << len(binary_str))  # Subtract 2^n for twos complement

binary_number = "01011001011001010111001100100001"
decimal_value = twos_complement_to_decimal(binary_number)
print(f"Two's Complement Decimal Value: {decimal_value}")

# E)


def ieee_754_to_float(binary_str):
    if len(binary_str) != 32:
        raise ValueError("Input must be a 32-bit binary string.")

    # Extract sign, exponent, and mantissa
    sign_bit = int(binary_str[0], 2)
    exponent_bits = binary_str[1:9]
    mantissa_bits = binary_str[9:]

    
    sign = (-1) ** sign_bit  # 0 means positive, 1 means negative

    # Compute the exponent
    exponent = int(exponent_bits, 2) - 127  # IEEE-754 uses a bias of 127

    # Compute the mantissa
    mantissa = 1  
    for i, bit in enumerate(mantissa_bits):
        mantissa += int(bit) * (2 ** -(i + 1))

    # Compute the final float value
    float_value = sign * mantissa * (2 ** exponent)

    return float_value


# Given binary number:
binary_number = "01011001011001010111001100100001"

# Convert IEEE-754 to decimal float
result = ieee_754_to_float(binary_number)
print(f"IEEE-754 Representation: {result}")


# 4)

print("_________ Start of Question 4 __________")


def string_to_ascii(input_string):
    #Convert a string to its ASCII representation
    if input_string is None:
        return "Error: Null input"
    if not isinstance(input_string, str):
        return "Error: Input must be a string"
    
    return [ord(char) for char in input_string]

#Converts each character in the input string to its ASCII representation using ord().
#Handles cases where input is None or not a string.


def ascii_to_string(ascii_list):
    #Convert a list of ASCII values back to a string 
    if ascii_list is None:
        return "Error: Null input"
    if not isinstance(ascii_list, list) or not all(isinstance(i, int) for i in ascii_list):
        return "Error: Input must be a list of ASCII values"
    
    try:
        return ''.join(chr(i) for i in ascii_list)
    except ValueError:
        return "Error: Invalid ASCII values in list"
    
#Converts a list of ASCII values back into a string using chr().
#Ensures the input is a valid list of integers before processing.

# Test cases
test_strings = ["hello", "ABC", "", "123", "!@#", "a b c", None]
test_ascii_lists = [[104, 101, 108, 108, 111], [65, 66, 67], [], 
                    [49, 50, 51], [33, 64, 35], [97, 32, 98, 32, 99], None]

print("Q4: ASCII Conversion\n")

# Test string to ASCII
print("String to ASCII:")
for test in test_strings:
    print(f'Input: {repr(test)} -> ASCII Output: {string_to_ascii(test)}')

print("\nASCII to String:")
# Test ASCII to string
for test in test_ascii_lists:
    print(f'Input: {test} -> String Output: {ascii_to_string(test)}')



# 5)

print("_________ Start of Question 5 __________")


def string_to_unicode():
    # Prompt the user for a string and convert it to Unicode code points 
    input_string = input("Enter a string to convert to Unicode (or type 'q' to quit): ").strip()
    
    if input_string.lower() == "q":
        return None

    if input_string == "":
        return []

    return [ord(char) for char in input_string]

def unicode_to_string():
    # Prompt the user for a list of Unicode values and convert it to a string
    input_unicode = input("Enter a list of Unicode values (comma-separated) or type 'q' to quit: ").strip()
    
    if input_unicode.lower() == "q":
        return None

    try:
        unicode_list = [int(value.strip()) for value in input_unicode.split(",") if value.strip()]
        return ''.join(chr(i) for i in unicode_list)
    except ValueError:
        return "Error: Invalid input! Please enter only integer Unicode values."

# Main interactive loop
while True:
    print("\nChoose an option:")
    print("1 - Convert String to Unicode")
    print("2 - Convert Unicode List to String")
    print("3 - Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        result = string_to_unicode()
        if result is not None:
            print(f"Unicode Output: {result}")
    
    elif choice == "2":
        result = unicode_to_string()
        if result is not None:
            print(f"String Output: {result}")
    
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")





# Skeleton code:
"""
def string_to_unicode(input_string):
    # Convert a string to its Unicode code points 
    if input_string is None:
        return "Error: Null input"
    if not isinstance(input_string, str):
        return "Error: Input must be a string"

    return [ord(char) for char in input_string]

def unicode_to_string(unicode_list):
    # Convert a list of Unicode code points back to a string
    if unicode_list is None:
        return "Error: Null input"
    if not isinstance(unicode_list, list):
        return "Error: Input must be a list of Unicode values"
    
    # Ensure all elements are integers
    if not all(isinstance(i, int) for i in unicode_list):
        return "Error: Non-integer value in list"

    try:
        return ''.join(chr(i) for i in unicode_list)
    except ValueError:
        return "Error: Invalid Unicode values in list"

# Test cases
test_strings = ["hello", "ABC", "", "a b c", None]
test_unicode_lists = [
    [104, 101, 108, 108, 111], 
    [65, 66, 67], 
    [], 
    [256, 300], 
    [104, 'abc', 108, 108, 111], 
    None
]

print("Q5: Unicode Conversion\n")

# Test string to Unicode
print("String to Unicode:")
for test in test_strings:
    print(f'Input: {repr(test)} -> Unicode Output: {string_to_unicode(test)}')

print("\nUnicode to String:")
# Test Unicode to string
for test in test_unicode_lists:
    print(f'Input: {test} -> String Output: {unicode_to_string(test)}')

    """