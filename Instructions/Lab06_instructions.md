# Lab 06: Breadth-First Search

## Overview
In this lab, you will implement **Breadth-First Search (BFS)** from Chapter 6 of "Grokking Algorithms." BFS is used to find the shortest path in unweighted graphs.

## Learning Objectives
- Understand graph representation using adjacency lists
- Implement BFS using a queue
- Find shortest paths in unweighted graphs
- Avoid infinite loops by tracking visited nodes

## Background

### Graphs
A graph consists of:
- **Nodes** (vertices): The entities
- **Edges**: Connections between nodes

Graphs can be:
- **Directed**: Edges have direction (A → B doesn't mean B → A)
- **Undirected**: Edges go both ways

### BFS Algorithm
BFS explores nodes level by level:
1. Start at the source node
2. Visit all neighbors (distance 1)
3. Then visit neighbors of neighbors (distance 2)
4. Continue until target found or all nodes visited

**Key insight**: BFS finds the shortest path because it explores closer nodes first!

### Queue (FIFO)
BFS uses a queue (First In, First Out):
- Add new nodes to the back
- Process nodes from the front
- This ensures we check closer nodes before farther ones

## Your Tasks

### Task 1: Implement `search()`
Find a mango seller (name ends with 'm') using BFS:
- Create a queue with the start node's neighbors
- Track searched nodes to avoid infinite loops
- While queue is not empty:
  - Pop from front
  - If not already searched:
    - Check if they're a mango seller
    - If not, add their neighbors to queue
    - Mark as searched
- Return the seller's name or `None`

### Task 2: Implement `bfs_shortest_path()`
Find the shortest path from start to end:
- Queue stores `(node, path_to_node)` tuples
- When you reach the end node, return the path
- Return `None` if no path exists

## Example

```python
graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

>>> search(graph, "you")
'thom'  # thom ends with 'm'

>>> bfs_shortest_path(graph, "you", "thom")
['you', 'claire', 'thom']
```

## Testing
```bash
python -m pytest tests/ -v
```

## Hints
- Use `collections.deque` for an efficient queue
- `deque.popleft()` removes from front, `deque.append()` adds to back
- Use a `set` to track visited nodes (O(1) lookup)
- Check if a node is searched BEFORE processing it

## Common Mistakes
- Forgetting to mark nodes as searched → infinite loop!
- Checking if searched AFTER processing → duplicate work
- Using a list instead of deque → slow `pop(0)` operation

## Submission
Commit and push your completed `bfs.py` file.
