# 1. Write a  Python program to calculate the sum of a list of numbers using recursion


def sum_of_num(array):
    for i in range (len(array)):
        if len(array) == 1:
            return array[0]
        
        else:
            return array[0] + sum_of_num(array[1:])  # Recursively sum the rest of the array

print(sum_of_num([23, 34, 56, 71]))
print(sum_of_num([5]))
