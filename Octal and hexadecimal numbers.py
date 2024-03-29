'''
There are two additional conventions in Python that are unknown to the world of mathematics. The first allows us to use numbers in an octal representation.

If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.

0o123 is an octal number with a (decimal) value equal to 83.

The print() function does the conversion automatically. Try this:
'''
print(0o123) # oct(123) = 83
# OR
print(0O123)

######################

'''
The second convention allows us to use hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).

0x123 is a hexadecimal number with a (decimal) value equal to 291. The print() function can manage these values too. Try this:
'''
print(0x123) # hex(123) = 291
# OR
print(0X123)

