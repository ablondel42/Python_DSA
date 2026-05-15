from typing import Optional, List

class BinaryNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional['BinaryNode'] = None
        self.right: Optional['BinaryNode'] = None

def in_order_search(head: Optional[BinaryNode]) -> List[int]:
    pass
