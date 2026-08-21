def bubble_sort(arr):
    n = len(arr)  # Total number of elements in the list
    
    # OUTER LOOP: Controls the number of passes.
    # We use 'n - 1' because with 'n' elements, after locking (n - 1) items 
    # into place, the 1 remaining item is automatically sorted.
    for i in range(n - 1):
        
        # INNER LOOP: Compares adjacent pairs (arr[j] and arr[j + 1]).
        # 1. The '- 1' prevents IndexError so arr[j + 1] doesn't look past the last index.
        # 2. The '- i' skips comparing elements at the end that were already 
        #    locked into place in previous passes.
        for j in range(n - 1 - i):
            
            # If the left element is larger than the right, swap them
            if arr[j] > arr[j + 1]:
                # Pythonic swap (simultaneously updates both positions)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

s = bubble_sort([5, 4, 6, 2, 1, 9])
print(s)  # Output: [1, 2, 4, 5, 6]