def bubble_sort_while(arr):
    n = len(arr)
    
    i = 0
    # OUTER WHILE LOOP: Replaces 'for i in range(n - 1)'
    # Keeps track of the number of completed passes (runs until i = n - 1)
    while i < n - 1:
        
        j = 0
        # INNER WHILE LOOP: Replaces 'for j in range(n - 1 - i)'
        # Compares adjacent elements, stopping before the already-sorted end elements
        while j < n - 1 - i:
            
            # If current element is greater than next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
            j += 1  # Increment inner counter (move to next adjacent pair)
            
        i += 1      # Increment outer counter (move to next pass)
        
    return arr  # Return the sorted list

# Call and test the function
s = bubble_sort_while([5, 4, 6, 2, 1])
print(s)  # Output: [1, 2, 4, 5, 6]
