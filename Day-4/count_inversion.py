def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   
    left = low  
    right = mid + 1 

    cnt = 0     

    
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  
            right += 1

    
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    
    while (right <= high):
        temp.append(arr[right])
        right += 1

    
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt  

def mergeSort(arr : List[int], low : int, high : int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)    
    cnt += mergeSort(arr, mid + 1, high)  
    cnt += merge(arr, low, mid, high)  
    return cnt

def numberOfInversions(a : List[int], n : int) -> int:
    n = len(a)
    return mergeSort(a, 0, n - 1)