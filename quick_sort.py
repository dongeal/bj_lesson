import sys
sys.stdin = open("input.txt","r")

data = list(map(int, input().split()))

print(data)

def quick(data , start, end):
    if  start >= end:
        return
    key = start
    left = start + 1
    right = end
    
    while left<=right :
        
        while left <= end and data[left] <= data[key] :
            left += 1
        
        while right > start and data[right] >= data[key] :
            right -= 1

        if  left > right:
            data[right], data[key] = data[key], data[right]
        else:
            data[left], data[right] = data[right], data[left]
    quick(data, start, right - 1)
    quick(data, right +1 , end)

quick(data, 0, len(data)-1)

print(data)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
def quick_sort(array):
    
    #리스트가 하나 이하의 원소만 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트 
    
    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
    print(left_side)
    print(pivot)
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분
    print(right_side)
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
