import random

alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

number = '0123456789'
special_char = '@!#$%&*()=+\/;:~'

use_all = alpha_lower + alpha_upper + number + special_char

len_pass = 8

password = ''.join(random.sample(use_all, len_pass))

print("Your generated password is"+password)
