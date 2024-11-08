print("Insert options for decisions. Type \"done\" to quit.")

options = []
inputValue = input("")
while inputValue.lower() != "done":
    options.append(inputValue)
    inputValue = input()

# Python3 implementation of QuickSort


# Function to find the partition position
def partition(array, low, high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        response = input(f"{array[j]} or {pivot} ")
        if response == "2" or response.lower() == pivot.lower():
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# Function to perform quicksort


def quick_sort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


print("Type the name of the option you would want. You can also type 1 or 2 for left and right respectively.")
quick_sort(options, 0, len(options) - 1)

options.reverse()
print("Your options sorted are the following:")
counter = 1
for option in options:
    print(str(counter) + "\t" + option)
    counter += 1

delayInput = input()