# Binary sort
lst = [i for i in range(101)]


def binary_sort(list, item):
    low = 0
    high = len(list) - 1
    steps = 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        steps += 1

        if guess == item:
            return f"Item found {steps}"
        if item >= guess:
            low = mid + 1
        else:
            high = mid - 1

    return "Not found"


print(binary_sort(lst, 50))


# Selection sort
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return  smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 1, 10, 8]))