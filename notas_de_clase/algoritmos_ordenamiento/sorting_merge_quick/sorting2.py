def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j] :
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while i < len(left):
        result.append(left[i])
        i = i + 1
    while j < len(right):
        result.append(right[j])
        j = j + 1
    return result

def mergesort(l):
    if len(l) < 2:
        return l[:]
    else:
        middle = len(l) // 2
        left = mergesort(l[:middle])
        right = mergesort(l[middle:])
        together = merge(left, right)
        return together



# no recursivo
def mergeSortNR(list):
    # start with least partition size of 2^0 = 1
    width = 1   
    n = len(list)                                          
    # subarray size grows by powers of 2 
    # since growth of loop condition is exponential, 
    # time consumed is logarithmic (log2n)

    while (width < n):
        # always start from leftmost
        l=0
        while (l < n): 
            r = min(l+(width*2-1), n-1)         
            m = min(l+width-1,n-1)
            print(l,r,m)
            # final merge should consider 
            # unmerged sublist if input arr
            # size is not power of 2              
            mergeNR(list, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return list
   
# Merge Function 

def mergeNR(a, l, m, r): 
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 

    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1

    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1

    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
 

 ## quicksort
# Partition function

def partition(list, low, high):
    # Choose the pivot
    pivot = list[high]
    # Index of smaller element and indicates 
    # the right position of pivot found so far
    i = low - 1

    # Traverse list[low..high] and move all smaller
    # elements to the left side. Elements from low to 
    # i are smaller after every iteration

    for j in range(low, high):
        if list[j] < pivot:
            i += 1
            swap(list, i, j)

    # Move pivot after smaller elements and
    # return its position
    swap(list, i + 1, high)
    return i + 1


# Swap function
def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

# The QuickSort function implementation
def quickSort(list, low, high):
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(list, low, high)
        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(list, low, pi - 1)
        quickSort(list, pi + 1, high)


## quicksort no recursivo 

def partitionNR(list,l,h):
    i = ( l - 1 )
    x = list[h]
    
    for j in range(l , h):
        if list[j] <= x:
 
            # increment index of smaller element
            i = i+1
            list[i],list[j] = list[j],list[i]
 
    list[i+1],list[h] = list[h],list[i+1]
    return (i+1)
 
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quickSortIterative(list,l,h):
 
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
 
    # initialize top of stack
    top = -1
 
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
 
        # Set pivot element at its correct position in
        # sorted array
        p = partition( list, l, h )
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h