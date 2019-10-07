# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for numba in range(len(arr)-1):
        temp = arr[numba]
        for i in range(1+numba, len(arr)):
            if temp > arr[i]:
                # Put to temp2 variable
                temp2 = arr[i]
                # Replace el in current list, l, with the temp varialbe
                arr[i] = temp
                # Replace temp with current lowest 
                temp = temp2
        # Replace list's number
        arr[numba] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr