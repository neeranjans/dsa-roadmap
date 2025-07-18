def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))

    for i in indexing_length:
        value_to_sort = list_a[i]

        # Move left as long as the value before is greater
        while list_a[i - 1] > value_to_sort and i > 0:
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]  # Swap
            i = i - 1  # Move left

    return list_a

# Example usage
arr = [12, 5, 6, 1, 9]
print("Original array:", arr)
sorted_arr = insertion_sort(arr)
print("Sorted array:  ", sorted_arr)

