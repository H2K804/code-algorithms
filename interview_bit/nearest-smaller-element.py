# https://www.interviewbit.com/problems/nearest-smaller-element/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        small_stack = [-1]
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                small_stack.append(A[i-1])
            else:
                j = i - 1
                while j >= 0:
                    if small_stack[j] < A[i]:
                        small_stack.append(small_stack[j])
                        break
                    j -= 1
        return small_stack
            
