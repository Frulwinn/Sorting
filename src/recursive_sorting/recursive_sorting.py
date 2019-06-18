# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    #loop through list of elements
    for i in range(elements)

        #if all elements in arrA have been merged, 
        if a >= len(arrA):
            #put next element in arrB into merged array
            merged_arr[i] = arrB[b]
            b += 1
        #elif all elements in arrB have been merged, 
        elif b >= len(arrB):
            #put next element in arrA into merged array
            merged_arr[i] = arrA[a]
            b += 1
        #elif next element in arrA smaller, add to merged array
        elif arrA[a] < arrB[b]
            #put the element from A into the output array
            merged_arr[i] = arrA[a]
            #increment the index
            a += 1
        #if A[0] is bigger than B[0]
        else: #arrA[a] >= arrB[b]:
            #put the element from B into the output array
            merged_arr[i] = arrB[b]
            b += 1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
