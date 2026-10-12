A = [10, 20, 30, 40]
last = A[-1]
for i in range(len(A)-1,0,-1):
    A[i] = A[i-1]
A[0] = last
print (A)
