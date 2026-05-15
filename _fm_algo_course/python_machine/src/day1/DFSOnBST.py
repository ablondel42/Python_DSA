from typing import Optional

class BSTNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

def dfs_on_bst(head: Optional[BSTNode], needle: int) -> bool:
    pass
