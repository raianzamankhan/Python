def bubble_sort_descending(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # CHANGE HERE: Use '<' instead of '>'
            # If the left element is SMALLER than the right element, swap them!
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

# Test descending sort
s = bubble_sort_descending([5, 4, 6, 2, 1])
print(s)  # Output: [6, 5, 4, 2, 1]