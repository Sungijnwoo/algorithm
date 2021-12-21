N, K = map(int, input().split())

li = list(map(int, input().split()))

def find_low_value(li, target, start, end):
    if start > end:
        return None
    
    middle = (start + end) // 2
    if (middle == 0 or li[middle-1] < target) and li[middle] == target:
        return middle
    
    elif li[middle] < target:
        return find_low_value(li, target, middle+1, end)
    
    elif li[middle] >= target:
        return find_low_value(li, target, start, middle-1)

def find_high_value(li, target, start, end):
    if start > end:
        return None

    middle = (start + end) // 2
    if (middle == N-1 or li[middle+1] > target) and li[middle] == target:
        return middle

    elif li[middle] <= target:
        return find_high_value(li, target, middle+1, end)
    
    elif li[middle] > target:
        return find_high_value(li, target, start, middle-1)

def count_value(li, target):
    low_idx = find_low_value(li, target, 0, len(li)-1)
    high_idx = find_high_value(li, target, 0, len(li)-1)
    print(low_idx, high_idx)
    if low_idx == None:
        print(-1)
    else:
        print(high_idx-low_idx+1)

count_value(li, K)



