

def bubble(unsorted_list):
    indexing_length = len(unsorted_list) - 1 #Save an Iteraction because last value will already be sorted
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if unsorted_list[i] > unsorted_list[i+1]: #if value in list is greater than value directly to the right of it,
                sorted = False # These values are unsorted
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i] #Switch these values
    return unsorted_list # Return our list "unsorted_list" which is not sorted.


print(bubble([4,8,1,14,8,2,9,5,7,6,6]))
