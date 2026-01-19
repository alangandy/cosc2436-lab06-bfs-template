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

---

## Complete Solutions

### Task 1: `search()` - Complete Implementation

```python
from collections import deque

def person_is_seller(name: str) -> bool:
    """
    Check if person is a mango seller.
    From Chapter 6: Name ends with 'm' = mango seller.
    """
    return name[-1] == 'm'


def search(graph: Dict[str, List[str]], start: str) -> Optional[str]:
    """
    Search for a mango seller using BFS.
    
    From Chapter 6 (page 114):
    - Use a queue to search in order
    - Mark people as searched to avoid infinite loops
    
    Args:
        graph: Adjacency list {person: [friends]}
        start: Starting person
    
    Returns:
        Name of mango seller if found, None otherwise
    """
    # Create a queue with the start node's neighbors
    search_queue = deque(graph[start])
    
    # Track who we've already searched (to avoid infinite loops)
    searched = set()
    
    while search_queue:
        # Pop the first person from the queue
        person = search_queue.popleft()
        
        # Only search if we haven't already
        if person not in searched:
            # Check if they're a mango seller
            if person_is_seller(person):
                return person
            else:
                # Not a seller - add their friends to the queue
                search_queue.extend(graph.get(person, []))
                # Mark this person as searched
                searched.add(person)
    
    # No mango seller found
    return None
```

**How it works:**
1. Create a queue initialized with the start node's neighbors
2. Create an empty set to track searched nodes
3. While the queue is not empty:
   - Pop the first person from the front (`popleft()`)
   - If we haven't searched them yet:
     - Check if they're a mango seller (name ends with 'm')
     - If yes: return their name
     - If no: add their friends to the queue and mark them as searched
4. If queue empties without finding a seller, return `None`

---

### Task 2: `bfs_shortest_path()` - Complete Implementation

```python
def bfs_shortest_path(graph: Dict[str, List[str]], start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Args:
        graph: Adjacency list
        start: Starting node
        end: Target node
    
    Returns:
        List of nodes in path, or None if no path exists
    """
    # Edge case: start is the end
    if start == end:
        return [start]
    
    # Queue stores (current_node, path_to_current_node)
    search_queue = deque([(start, [start])])
    
    # Track visited nodes
    visited = set([start])
    
    while search_queue:
        # Pop the first item from the queue
        current_node, path = search_queue.popleft()
        
        # Check all neighbors
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                # Build the new path
                new_path = path + [neighbor]
                
                # Check if we've reached the end
                if neighbor == end:
                    return new_path
                
                # Mark as visited and add to queue
                visited.add(neighbor)
                search_queue.append((neighbor, new_path))
    
    # No path found
    return None
```

**How it works:**
1. Handle edge case: if start equals end, return `[start]`
2. Create a queue of `(node, path_to_node)` tuples, starting with `(start, [start])`
3. Create a visited set initialized with the start node
4. While the queue is not empty:
   - Pop the first `(current_node, path)` from the queue
   - For each neighbor of the current node:
     - If not visited:
       - Build the new path: `path + [neighbor]`
       - If neighbor is the end: return the new path (shortest path found!)
       - Otherwise: mark as visited and add `(neighbor, new_path)` to queue
5. If queue empties without finding end, return `None`

---

## Example Usage

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

# Search for mango seller
>>> search(graph, "you")
'thom'  # thom ends with 'm'

# BFS explores in this order:
# Level 0: you
# Level 1: alice, bob, claire
# Level 2: peggy, anuj, peggy, thom, jonny
# 'thom' ends with 'm' - found!

# Shortest path
>>> bfs_shortest_path(graph, "you", "thom")
['you', 'claire', 'thom']

>>> bfs_shortest_path(graph, "you", "anuj")
['you', 'bob', 'anuj']

>>> bfs_shortest_path(graph, "you", "you")
['you']

>>> bfs_shortest_path(graph, "you", "nonexistent")
None
```

---

## Testing
```bash
python -m pytest tests/ -v
```

## Submission
Commit and push your completed `bfs.py` file.
