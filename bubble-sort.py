def bubble_sort(arr):
    n = len(arr)
    
    # Outer loop: number of passes (n-1 passes needed)
    for i in range(n-1):
        
        # Inner loop: compare adjacent elements
        # We reduce the range each time because the largest elements 
        # are already in their correct positions
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if elements are in wrong order
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
