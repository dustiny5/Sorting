# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []
    
    while len(arrA) != 0 or len(arrB) != 0:
        if len(arrA)== 0 and len(arrB) == 0:
            return merged_arr
            break

        elif len(arrA) == 0 and len(arrB) == 1:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])

        elif len(arrA) == 1 and len(arrB) == 0:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])

        elif len(arrA) > 1 and len(arrB) == 0:
            for el in arrA:
                merged_arr.append(el)
                arrA.remove(el)
                break

        elif len(arrA) == 0 and len(arrB) > 1:
            for it in arrB:
                merged_arr.append(it)
                arrB.remove(it)
                break

        elif arrA[0]>arrB[0]:
            merged_arr.append(arrB[0])
            arrB.remove(arrB[0])

        else:
            merged_arr.append(arrA[0])
            arrA.remove(arrA[0])
      
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) == 1:
        return arr
    else:
        # Divide the list to half until we get single list of elements
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])    
      
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
