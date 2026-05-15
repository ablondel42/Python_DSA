from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.length: int = 0
        pass

    def push(self, item: T) -> None:
        pass

    def pop(self) -> Optional[T]:
        pass

    def peek(self) -> Optional[T]:
        pass
