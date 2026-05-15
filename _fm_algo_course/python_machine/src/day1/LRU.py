from typing import Generic, TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class LRU(Generic[K, V]):
    def __init__(self, capacity: int = 10) -> None:
        pass

    def update(self, key: K, value: V) -> None:
        pass

    def get(self, key: K) -> Optional[V]:
        pass
