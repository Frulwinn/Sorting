# TO-DO: Complete the selection_sort() function below 

m = [1, 2, 5, 8, 10, 13, 15, 4, 19, 7, 20]

def selection_sort( arr ):
    
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # Loop through each index from the current through the end of the array
        for each_index in range(cur_index, len(arr)):

            # If the element at the index in the array we are looking at is smaller than the element 
            # in the index holding the smallest...
            if arr[each_index] < arr[smallest_index]:

                # set the actual index of the smallest to the index we are looking at
                smallest_index = each_index 

                # set the element in the smallest_index to the element that's in the current index
                arr[smallest_index] = arr[cur_index]

        # TO-DO: swap
        arr[cur_index] = smallest_index

     return arr

print(selection_sort(m))    


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr