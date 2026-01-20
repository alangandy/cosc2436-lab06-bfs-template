# Lab 6: Breadth-First Search

## 1. Introduction and Objectives

### Overview
Implement breadth-first search (BFS) to find shortest paths in graphs. Build a road network connecting Texas cities.

### Learning Objectives
- Understand graph data structures
- Implement BFS algorithm
- Find shortest path (fewest edges)
- Use queues for level-order traversal

### Prerequisites
- Complete Labs 1-5
- Read Chapter 6 in "Grokking Algorithms" (pages 101-120)

---

## 2. Algorithm Background

### Graphs
- **Nodes/Vertices**: Things (cities)
- **Edges**: Connections (roads)
- **Directed vs Undirected**

### BFS Properties
- Explores level by level
- Uses a **queue** (FIFO)
- Finds shortest path by edges
- Time: O(V + E) where V=vertices, E=edges

---

## 3. Project Structure

```
lab06_bfs/
├── graph.py       # Graph implementation
├── bfs.py         # BFS algorithm
├── main.py        # Main program
└── README.md      # Your lab report
```

---

## 4. Step-by-Step Implementation

### Step 1: Create `graph.py`

```python
"""
Lab 6: Graph Implementation
Adjacency list representation for city road network.
"""
from typing import Dict, List, Set
from collections import defaultdict


class Graph:
    """
    Undirected graph using adjacency list.
    
    Adjacency list: Each node stores list of neighbors
    - Space efficient for sparse graphs
    - O(1) to add edge
    - O(degree) to check if edge exists
    """
    
    def __init__(self):
        # defaultdict creates empty list for new keys
        self.adjacency_list: Dict[str, List[str]] = defaultdict(list)
        self.vertices: Set[str] = set()
    
    def add_vertex(self, vertex: str) -> None:
        """Add a vertex to the graph."""
        self.vertices.add(vertex)
    
    def add_edge(self, v1: str, v2: str) -> None:
        """
        Add undirected edge between v1 and v2.
        For directed graph, only add v1 -> v2.
        """
        self.vertices.add(v1)
        self.vertices.add(v2)
        
        # Undirected: add both directions
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
        if v1 not in self.adjacency_list[v2]:
            self.adjacency_list[v2].append(v1)
    
    def get_neighbors(self, vertex: str) -> List[str]:
        """Get all neighbors of a vertex."""
        return self.adjacency_list[vertex]
    
    def has_edge(self, v1: str, v2: str) -> bool:
        """Check if edge exists between v1 and v2."""
        return v2 in self.adjacency_list[v1]
    
    def display(self) -> None:
        """Display the graph structure."""
        print("\nGraph Adjacency List:")
        print("-" * 40)
        for vertex in sorted(self.vertices):
            neighbors = self.adjacency_list[vertex]
            print(f"{vertex}: {neighbors}")
    
    def __len__(self) -> int:
        return len(self.vertices)


def create_texas_road_network() -> Graph:
    """
    Create a simplified Texas highway network.
    Edges represent direct highway connections.
    """
    g = Graph()
    
    # Major highway connections (simplified)
    roads = [
        # I-45 corridor
        ("Houston", "Dallas"),
        
        # I-35 corridor  
        ("Dallas", "Austin"),
        ("Austin", "San Antonio"),
        ("San Antonio", "Laredo"),
        
        # I-10 corridor
        ("Houston", "San Antonio"),
        ("San Antonio", "El Paso"),
        
        # I-20 corridor
        ("Dallas", "Fort Worth"),
        ("Fort Worth", "Lubbock"),
        ("Lubbock", "El Paso"),
        
        # Other connections
        ("Dallas", "Arlington"),
        ("Fort Worth", "Arlington"),
        ("Houston", "Corpus Christi"),
        ("Corpus Christi", "San Antonio"),
        ("Austin", "Killeen"),
        ("Dallas", "Plano"),
        ("Dallas", "Irving"),
        ("Dallas", "Garland"),
        ("Plano", "Frisco"),
        ("Plano", "McKinney"),
        ("Corpus Christi", "Brownsville"),
        ("Brownsville", "McAllen"),
        ("McAllen", "Laredo"),
    ]
    
    for city1, city2 in roads:
        g.add_edge(city1, city2)
    
    return g
```

### Step 2: Create `bfs.py`

```python
"""
Lab 6: Breadth-First Search Implementation
Finds shortest path (by number of edges) in unweighted graph.

From Chapter 6: BFS answers two questions:
1. Is there a path from A to B?
2. What is the shortest path from A to B?
"""
from typing import List, Dict, Optional, Callable
from collections import deque
from graph import Graph


# ============================================
# MANGO SELLER EXAMPLE FROM CHAPTER 6
# ============================================
def person_is_seller(name: str) -> bool:
    """
    Check if person is a mango seller.
    From Chapter 6: Name ends with 'm' = mango seller.
    """
    return name[-1] == 'm'


def search_for_seller(graph: dict, start: str) -> Optional[str]:
    """
    Search for a mango seller using BFS.
    
    From Chapter 6 (page 114):
    - Use a queue to search in order
    - Mark people as searched to avoid infinite loops
    - First-degree connections searched before second-degree
    """
    search_queue = deque()
    search_queue += graph[start]
    searched = set()  # Track who we've already searched
    
    while search_queue:
        person = search_queue.popleft()
        
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return person
            else:
                search_queue += graph.get(person, [])
                searched.add(person)
    
    print("No mango seller found!")
    return None


def bfs_find_path(graph: Graph, start: str, end: str) -> Optional[List[str]]:
    """
    Find shortest path from start to end using BFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    
    Returns:
        List of vertices forming the path, or None if no path exists
    """
    if start not in graph.vertices or end not in graph.vertices:
        print(f"Error: '{start}' or '{end}' not in graph")
        return None
    
    # Queue stores (current_vertex, path_to_current)
    queue = deque([(start, [start])])
    
    # Track visited vertices to avoid cycles
    visited = {start}
    
    print(f"\nBFS from '{start}' to '{end}':")
    print("-" * 40)
    
    level = 0
    nodes_at_level = 1
    next_level_nodes = 0
    
    while queue:
        current, path = queue.popleft()
        nodes_at_level -= 1
        
        print(f"Level {level}: Visiting '{current}'")
        
        # Found the destination!
        if current == end:
            print(f"\nFound path with {len(path) - 1} edges!")
            return path
        
        # Explore neighbors
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                next_level_nodes += 1
        
        # Track levels for visualization
        if nodes_at_level == 0:
            level += 1
            nodes_at_level = next_level_nodes
            next_level_nodes = 0
    
    print(f"\nNo path found from '{start}' to '{end}'")
    return None


def bfs_all_reachable(graph: Graph, start: str) -> Dict[str, int]:
    """
    Find all vertices reachable from start and their distances.
    
    Returns:
        Dict mapping vertex -> distance from start
    """
    if start not in graph.vertices:
        return {}
    
    distances = {start: 0}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        current_dist = distances[current]
        
        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)
    
    return distances


def bfs_is_connected(graph: Graph, v1: str, v2: str) -> bool:
    """Check if path exists between two vertices."""
    path = bfs_find_path(graph, v1, v2)
    return path is not None
```

### Step 3: Create `main.py`

```python
"""
Lab 6: Main Program
Demonstrates BFS on Texas road network.
"""
from graph import Graph, create_texas_road_network
from bfs import bfs_find_path, bfs_all_reachable


def main():
    # =========================================
    # PART 1: Mango Seller Example (from Chapter 6)
    # =========================================
    print("=" * 60)
    print("PART 1: MANGO SELLER SEARCH (Chapter 6)")
    print("=" * 60)
    
    from bfs import search_for_seller
    
    # Graph from Chapter 6 - your friends network
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
    
    print("\nFriends network:")
    for person, friends in graph.items():
        print(f"  {person} → {friends}")
    
    print("\nSearching for mango seller (name ends with 'm')...")
    search_for_seller(graph, "you")
    
    # =========================================
    # PART 2: Create Road Network
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: TEXAS ROAD NETWORK GRAPH")
    print("=" * 60)
    
    roads = create_texas_road_network()
    print(f"\nCreated graph with {len(roads)} cities")
    roads.display()
    
    # =========================================
    # PART 2: Find Shortest Paths
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: SHORTEST PATH (BFS)")
    print("=" * 60)
    
    # Houston to El Paso
    path = bfs_find_path(roads, "Houston", "El Paso")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # Houston to McKinney
    print("\n" + "-" * 40)
    path = bfs_find_path(roads, "Houston", "McKinney")
    if path:
        print(f"\nRoute: {' → '.join(path)}")
    
    # =========================================
    # PART 3: Reachability
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: DISTANCES FROM HOUSTON")
    print("=" * 60)
    
    distances = bfs_all_reachable(roads, "Houston")
    
    print("\nCities by distance (edges) from Houston:")
    for dist in range(max(distances.values()) + 1):
        cities_at_dist = [c for c, d in distances.items() if d == dist]
        if cities_at_dist:
            print(f"  {dist} edge(s): {', '.join(sorted(cities_at_dist))}")
    
    # =========================================
    # PART 4: Key Concepts
    # =========================================
    print("\n" + "=" * 60)
    print("PART 4: BFS KEY CONCEPTS")
    print("=" * 60)
    print("""
    Why BFS finds shortest path:
    1. Explores ALL nodes at distance 1 first
    2. Then ALL nodes at distance 2
    3. And so on...
    
    First time we reach destination = shortest path!
    
    BFS uses a QUEUE (FIFO):
    - First In, First Out
    - Process nodes in order they were discovered
    
    Time Complexity: O(V + E)
    - Visit each vertex once: O(V)
    - Check each edge once: O(E)
    
    Note: BFS finds shortest path by NUMBER OF EDGES.
    For weighted graphs (actual distances), use Dijkstra's (Lab 9)!
    """)


if __name__ == "__main__":
    main()
```

---

## 5. Lab Report Template

```markdown
# Lab 6: Breadth-First Search

## Student Information
- **Name:** [Your Name]
- **Date:** [Date]

## Graph Concepts

### Adjacency List Representation
[Explain how the graph is stored]

### BFS Algorithm Steps
1. [Step 1]
2. [Step 2]
3. [Continue...]

## Test Results

| Start | End | Path | Edges |
|-------|-----|------|-------|
| Houston | El Paso | | |
| Houston | McKinney | | |
| Dallas | Laredo | | |

## Reflection Questions

1. Why does BFS use a queue instead of a stack?

2. What's the difference between BFS shortest path and actual shortest distance?

3. When would you use BFS vs DFS?
```

---

## 6. Submission
Save files in `lab06_bfs/`, complete README, commit and push.
