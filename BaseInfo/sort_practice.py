import random;
def bubble_sort(arr):
    nlen = len(arr);
    for i in range(nlen - 1):
        for j in range(nlen - i -1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j];
    return(arr);


numbers = [3, 1, 5, 8, -1];
print(f"numbers type is {type(numbers)}");
nums = bubble_sort(numbers);
print(f"\nbubble_sort: numbers: {numbers}, \nnum:{nums}");

def selection_sort(arr):
    nlen = len(arr);
    for i in range(nlen-1):
        minIndex = i;
        for j in range(i + 1, nlen):
            if arr[j] < arr[minIndex]:
                minIndex = j;
        arr[i], arr[minIndex]= arr[minIndex], arr[i];

selection_sort_data = [];
for i in range(10):
    selection_sort_data.append(random.randint(1, 100));

print(f"\nselection_sort_data: {selection_sort_data}");
selection_sort(selection_sort_data);
print(f"\nselection_sort_data after sort: {selection_sort_data}");

def quick_sort(arr):
    nlen = len(arr)    
    if nlen < 2:
        return arr
    pivot = arr[nlen // 2]
    left = [x for x in arr if x < pivot] 
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
    
quick_sort_data = [];
for i in range(10):
    quick_sort_data.append(random.randint(1, 100));

print(f"\nquick_sort_data: {quick_sort_data}");
sort_data = quick_sort(quick_sort_data);
print(f"\nquick_sort_data after sort: {sort_data}");