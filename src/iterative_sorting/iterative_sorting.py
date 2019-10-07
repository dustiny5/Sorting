# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for numba in range(len(arr)-1):
        # Compare number
        compare = arr[numba]

        # No need to iterate previous numbers since we've found the smallest number and replaced it **
        for i in range(1+numba, len(arr)):
            if compare > arr[i]:
                # Put to temp2 variable
                temp2 = arr[i]
                # Replace el in current list, l, with the temp varialbe
                arr[i] = compare
                # Replace temp with current lowest 
                compare = temp2
        # Replace list's number with the smallest number after iterating **
        arr[numba] = compare

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    start = arr[0]
    for i in range(1, len(arr)):
        if start > arr[i]:
            # Get temp value
            temp = start
            
            # Change to current 
            start = arr[i]
            
            # Swap numbers in list
            arr[i] = temp
            arr[i-1] = start
            
            # Change start to swapped number
            start = arr[i]

        elif start < arr[i]:
            start = arr[i]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr