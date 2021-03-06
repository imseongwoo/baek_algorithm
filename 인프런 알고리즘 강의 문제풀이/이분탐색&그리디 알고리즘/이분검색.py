def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None
n,m = list(map(int,input().split()))
array = list(map(int,input().split()))
array.sort()

result = binary_search(array,m,0,n-1)

print(result+1)
