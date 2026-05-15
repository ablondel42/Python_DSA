from typing import Optional

class BinaryNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional['BinaryNode'] = None
        self.right: Optional['BinaryNode'] = None

def compare_binary_trees(a: Optional[BinaryNode], b: Optional[BinaryNode]) -> bool:
    pass
