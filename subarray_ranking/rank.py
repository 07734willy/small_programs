A = [1, 5, 2, 4, 3, 6, 4, 9, 11, 8]
B = [2, 0, 1]
m = len(A)
n = len(B)
for i in range(m - n + 1):
    current_subarray = A[i:i + n]
    # we now do n - 1 comparaisons to check whether the subarray is correctly ordered.
    for B_index in range(n - 1):
        if current_subarray[B[B_index]] > current_subarray[B[B_index + 1]]:
            break
    else:
        print("Subarray found:", current_subarray)
