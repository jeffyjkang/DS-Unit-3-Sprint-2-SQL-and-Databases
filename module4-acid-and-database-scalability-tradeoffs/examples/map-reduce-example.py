# simplified map reduce example for horizontal scaling
from functools import reduce

my_list = [1, 2, 3, 4]

computer1_list = [1, 2]
computer2_list = [3, 4]

# how to find ssv
# step 1: square everything
# step 2: sum together

# traditional way to find sum of squared values
ssv_trad = sum([i**2 for i in my_list])

# map reduce
# cp_1_squared_values = map(lambda i: i**2, computer1_list) # cp_1_list = [1, 4]
# cp_2_squared_values = map(lambda i: i**2, computer2_list) # cp_2_list = [9, 16]

# squared_values = map(lambda i: i**2, my_list)

# def add_number(x1, x2):
#     return x1 + x2

# ssv_map_reduce = reduce(add_number, cp_1_squared_values, cp_2_squared_values)
# print('Sum of square values (trad): {}'.format(ssv_trad))
# print('Sum of square values (mapreduce): {}'.format())
