# Python Kata Machine

A Python port of the TypeScript Kata Machine - an interactive tool for learning data structures and algorithms.

## Setup

### Requirements
- Python 3.8+
- pip

### Installation

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test:
```bash
pytest tests/test_ArrayList.py
```

Run with verbose output:
```bash
pytest -v
```

## Project Structure

```
python_machine/
├── src/
│   └── day1/
│       ├── ArrayList.py
│       ├── Stack.py
│       ├── Queue.py
│       ├── SinglyLinkedList.py
│       ├── DoublyLinkedList.py
│       ├── BubbleSort.py
│       ├── QuickSort.py
│       ├── BinarySearchList.py
│       ├── LinearSearchList.py
│       ├── TwoCrystalBalls.py
│       ├── MazeSolver.py
│       ├── Map.py
│       ├── LRU.py
│       ├── MinHeap.py
│       ├── Trie.py
│       ├── DFSGraphList.py
│       ├── BFSGraphMatrix.py
│       ├── DFSOnBST.py
│       ├── BTPreOrder.py
│       ├── BTInOrder.py
│       ├── BTPostOrder.py
│       ├── BTBFS.py
│       └── CompareBinaryTrees.py
├── tests/
│       ├── test_ArrayList.py
│       ├── test_Stack.py
│       ├── test_Queue.py
│       ├── test_SinglyLinkedList.py
│       ├── test_DoublyLinkedList.py
│       ├── test_BubbleSort.py
│       ├── test_QuickSort.py
│       ├── test_BinarySearchList.py
│       ├── test_LinearSearchList.py
│       ├── test_TwoCrystalBalls.py
│       ├── test_MazeSolver.py
│       ├── test_Map.py
│       ├── test_LRU.py
│       ├── test_MinHeap.py
│       ├── test_Trie.py
│       ├── test_DFSGraphList.py
│       ├── test_BFSGraphMatrix.py
│       ├── test_DFSOnBST.py
│       ├── test_BTPreOrder.py
│       ├── test_BTInOrder.py
│       ├── test_BTPostOrder.py
│       ├── test_BTBFS.py
│       └── test_CompareBinaryTrees.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Data Structures

- ArrayList
- Stack
- Queue
- SinglyLinkedList
- DoublyLinkedList
- Map
- LRU Cache
- MinHeap
- Trie

## Algorithms

- Sorting: BubbleSort, QuickSort
- Searching: BinarySearch, LinearSearch, TwoCrystalBalls
- Graph Algorithms: DFSGraphList, BFSGraphMatrix, DFSOnBST
- Tree Traversals: Pre-order, In-order, Post-order, BFS
- Maze Solving

## How to Use

Each algorithm and data structure has a stub implementation with method signatures. Your task is to implement the functionality to pass the tests.

1. Pick an implementation file (e.g., `src/day1/ArrayList.py`)
2. Implement the required methods
3. Run the corresponding test file to verify your implementation
4. Repeat for other data structures and algorithms

## License

MIT
