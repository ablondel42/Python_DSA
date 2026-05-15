from typing import Generic, TypeVar, Optional

K = TypeVar('K')
V = TypeVar('V')

class Map(Generic[K, V]):
    def __init__(self) -> None:
        pass

    def set(self, key: K, value: V) -> None:
        pass

    def get(self, key: K) -> Optional[V]:
        pass

    def delete(self, key: K) -> Optional[V]:
        pass

    def has(self, key: K) -> bool:
        pass
