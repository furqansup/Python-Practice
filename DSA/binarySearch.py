# Binary Search


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        # Find the middle index
        mid = (low + high) // 2

        # Target found
        if arr[mid] == target:
            return mid

        # Search the right half
        elif arr[mid] < target:
            low = mid + 1

        # Search the left half
        else:
            high = mid - 1

    # Target not found
    return -1


arr = [2, 4, 6, 8, 10, 12]
target = 8

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")