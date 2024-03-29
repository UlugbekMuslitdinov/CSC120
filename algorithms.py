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
    return smallest_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 1, 10, 8]))


# Find the sum of the slist with recursion
def sumList(slist):
    if len(slist) != 0:
        current = slist.pop(0)
        total = current + sumList(slist)
        return total
    else:
        return 0


print(sumList([2, 4, 6]))


def binary_search(nums, item):
    low = nums[0]
    high = nums[len(nums)-1]
    mid = (low+high+1)//2
    print(nums)
    if item == mid:
        return "Item found!"
    elif item < mid:
        return binary_search([i for i in range(low, mid + 1)], item)
    elif item > mid:
        return binary_search([i for i in range(mid, high + 1)], item)


print(binary_search([i for i in range(101)], 9))


def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([10, 5, 2, 15, 67, 32, 76]))
