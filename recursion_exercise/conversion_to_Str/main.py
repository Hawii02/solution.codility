# Write a  Python program to convert an integer to a string in any base using recursion.

def int_to_string(n, base):
    convert_string = "0123456789ABCDEF"

    if n < base:
        # If 'n' is less than the base, return the corresponding character from the character set
        
        return convert_string[n]
    else:
        # If 'n' is greater than or equal to the base, recursively call the to_string function
        # to convert the quotient (n // base) to a string and concatenate it with the remainder
        # (n % base) represented in the character set

        return int_to_string(n // base, base) + convert_string[n % base]
print (int_to_string(2835, 16))