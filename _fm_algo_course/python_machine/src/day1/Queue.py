from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.length: int = 0
        pass

    def enqueue(self, item: T) -> None:
        pass

    def dequeue(self) -> Optional[T]:
        pass

    def peek(self) -> Optional[T]:
        pass
