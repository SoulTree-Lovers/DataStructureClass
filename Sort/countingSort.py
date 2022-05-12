def countingSort(A):
    k = max(A)
    c = [0 for _ in range(k+1)]
    for j in range(len(A)):
        c[A[j]] += 1
    for i in range(1, k+1):
        c[i] = c[i] + c[i-1]
    B = [0 for _ in range(len(A))]
    for j in range(len(A) - 1, -1, -1):
        B[c[A[j]] - 1] = A[j]
        c[A[j]] -= 1
    return B