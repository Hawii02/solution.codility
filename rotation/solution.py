# BDD
# GIVEN an array of N int
# THAT each element is shifted right by 1 index and last element of array moved to the first place
# WHEN array is rotated K times returns the array rotated in k times

# def solution(A, K):
#     if K == 0:
#         return A
#     else:
#         result = A[-K:] + A[:-K]
#     return result

# print(solution([1,2,3,4,5,6,7], 4))
# print(solution([0,0,0],1))
# print(solution([1,2,3,4],3))

def solution(A, K):
    # if K is greater than the length of the array, then we need to modify it by the length of the array
    # to get the correct number of rotations to perform on the array 
    k = K % len(A)
    # if k is 0, then we don't need to rotate the array
    if k == 0:
        return A
    # if k is less than the length of the array, then we need to rotate the array by k
    # to get the correct number of rotations to perform on the array  
    else:
        return A[-k:] + A[:-k]  # [-k:] is the last k elements of the array, 
                                #[:-k] is all the elements in the array except the last one ([-k:]) 
                                #eg [1,2,3,4,5,6,7,8,9,10] -> [1,2,3,4,5,6,7,8,9]

#Example
print(solution([3, 8, 9, 7, 6], 3))    #Output [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1))          #Output [0, 0, 0]
print(solution([1, 2, 3, 4], 4))       #Output [1, 2, 3, 4]