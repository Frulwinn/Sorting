# TO-DO: Complete the selection_sort() function below 

m = [5, 15, 3, 12, 17, 0]

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

                # set the element at the current index to the temporary var,
                # this is the smallest element
                arr[cur_index] = temp

        # TO-DO: swap
        arr[cur_index] = smallest_index

    return arr

print(selection_sort(m))    


# TO-DO:  implement the Bubble Sort function below

n = [1, 7, 9, 19, 16, 5, 2]
def bubble_sort( arr ):
    current_index = 0

    for i in range(0, len(arr) - 1):

        while arr[0]
        if arr[current_index] > arr[current_index + 1]:
            # Swap
            temp = arr[current_index]
            arr[current_index] = arr[current_index + 1]
            arr[current_index + 1] = temp

        current_index += 1

    return arr
print(bubble_sort(n))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr