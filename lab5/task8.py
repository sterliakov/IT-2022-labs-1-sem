def largest_rect(N, arr):
    best = min(arr) * N
    for i in range(N):
        for j in range(i+1, N+1):
            if i != j:
                best = max(best, min(arr[i:j]) * (j - i))
    return best
