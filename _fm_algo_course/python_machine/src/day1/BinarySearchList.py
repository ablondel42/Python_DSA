from typing import List

def binary_search(haystack: List[int], needle: int) -> bool:
    low, high = 0, len(haystack)

    while low < high:
        mid = low + (high - low) // 2
        val = haystack[mid]
        
        if val > needle:
            high = mid
        elif val < needle:
            low = mid + 1
        else:
            return True
        
    return False
