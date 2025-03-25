def max_min_select(arr):
    if len(arr) == 1:
        return arr[0], arr[0]  
    
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    
    mid = len(arr) // 2
    left_min, left_max = max_min_select(arr[:mid])
    right_min, right_max = max_min_select(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

if __name__ == "__main__":
    arr = [3, 1, 7, 9, 2, 8, 4, 6]
    min_val, max_val = max_min_select(arr)
    print(f"Menor elemento: {min_val}")
    print(f"Maior elemento: {max_val}")
