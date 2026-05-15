from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class SinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.length: int = 0
        pass

    def prepend(self, item: T) -> None:
        pass

    def insertAt(self, item: T, idx: int) -> None:
        pass

    def append(self, item: T) -> None:
        pass

    def remove(self, item: T) -> Optional[T]:
        pass

    def get(self, idx: int) -> Optional[T]:
        pass

    def removeAt(self, idx: int) -> Optional[T]:
        pass
