class Solution():
    def find3Numbers(self,A, arr_size, sum):
        for i in range(0, arr_size-1):
            # Try with first number = A[i] for all i except last
            s = set()
            curr_sum = sum - A[i] #Do this subtraction now to save time in loop
            #Try second number = A[j] for j = i+1..end
            for j in range(i + 1, arr_size):
                if (curr_sum - A[j]) in s:
                    #print("Triplet is", A[i],A[j],curr_sum-A[j])
                    return True
                s.add(A[j])
        return False

# Driver program to test above function 
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)
sol = Solution()
print(sol.find3Numbers(A, arr_size, sum))