from typing import List

def linear_search(haystack: List[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False
