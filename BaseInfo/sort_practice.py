import random
import time

def bubble_sort(arr):
    nlen = len(arr)
    for i in range(nlen - 1):
        for j in range(nlen - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    nlen = len(arr)
    for i in range(nlen - 1):
        minIndex = i
        for j in range(i + 1, nlen):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    sortData = [random.randint(1, 100) for _ in range(100)]
    print(f"Before sort (first 10): {sortData[:10]}")

    print("\nChoose algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Quick Sort")
    print("4. Merge Sort")

    choice = input("Enter number: ")
    start = time.time()

    if choice == "1":
        sortedData = bubble_sort(sortData[:])
    elif choice == "2":
        sortedData = selection_sort(sortData[:])
    elif choice == "3":
        sortedData = quick_sort(sortData[:])
    elif choice == "4":
        sortedData = merge_sort(sortData[:])
    else:
        print("Invalid choice.")
        return

    end = time.time()
    print(f"\nAfter sort  (first 10): {sortedData[:10]}")
    print(f"Time cost: {end - start:.6f}s")

if __name__ == "__main__":
    main()
