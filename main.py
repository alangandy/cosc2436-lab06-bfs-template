#!/usr/bin/env python3
"""
Lab 06: Breadth-First Search - Interactive Tutorial
====================================================

🎯 GOAL: Implement BFS in bfs.py

📚 BREADTH-FIRST SEARCH (Chapter 6):
------------------------------------
BFS answers two questions:
1. Is there a path from A to B?
2. What is the SHORTEST path from A to B?

KEY INSIGHT: BFS explores nodes level by level
- First: all nodes 1 step away
- Then: all nodes 2 steps away
- Then: all nodes 3 steps away...

This guarantees the first path found is the shortest!

HOW TO RUN:
-----------
    python main.py           # Run this tutorial
    python -m pytest tests/ -v   # Run the grading tests
"""

from collections import deque
from bfs import search, bfs_shortest_path, person_is_seller


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def graph_intro() -> None:
    """Introduce graphs and adjacency lists."""
    print_header("GRAPHS IN PYTHON")
    
    print("""
    A GRAPH has:
    - Nodes (vertices): things we're connecting
    - Edges: connections between nodes
    
    ADJACENCY LIST REPRESENTATION:
    We use a dictionary where:
    - Keys = nodes
    - Values = list of neighbors
    
    EXAMPLE - Social Network:
    
        you → alice → peggy
         ↓      ↓
        bob → anuj
         ↓
        claire → thom
                  ↓
               jonny
    
    In Python:
    """)
    
    graph = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": [],
    }
    
    print("    graph = {")
    for node, neighbors in graph.items():
        print(f'        "{node}": {neighbors},')
    print("    }")
    
    print("""
    READING THE GRAPH:
    - graph["you"] → ["alice", "bob", "claire"]  (your friends)
    - graph["bob"] → ["anuj", "peggy"]  (bob's friends)
    - graph["anuj"] → []  (anuj has no connections listed)
    """)


def queue_intro() -> None:
    """Introduce queues and deque."""
    print_header("QUEUES IN PYTHON")
    
    print("""
    BFS uses a QUEUE (First-In, First-Out = FIFO)
    
    Think of a line at a store:
    - First person in line gets served first
    - New people join at the back
    
    C++:   std::queue<string>
    Java:  Queue<String> = new LinkedList<>()
    Python: collections.deque
    
    WHY deque (not list)?
    - list.pop(0) is O(n) - slow!
    - deque.popleft() is O(1) - fast!
    
    OPERATIONS:
    -----------
    from collections import deque
    
    queue = deque()           # Create empty queue
    queue.append("alice")     # Add to back
    queue.append("bob")
    person = queue.popleft()  # Remove from front → "alice"
    """)
    
    # Live demo
    print("LIVE DEMO:")
    queue = deque()
    print(f"    queue = deque()  → {list(queue)}")
    queue.append("alice")
    print(f"    queue.append('alice')  → {list(queue)}")
    queue.append("bob")
    print(f"    queue.append('bob')  → {list(queue)}")
    queue.append("claire")
    print(f"    queue.append('claire')  → {list(queue)}")
    person = queue.popleft()
    print(f"    queue.popleft()  → '{person}', queue = {list(queue)}")


def demo_mango_seller() -> None:
    """Demonstrate the mango seller search."""
    print_header("PART 1: search() - Find the Mango Seller")
    
    print("""
    From Chapter 6: Find a mango seller in your network.
    Rule: A person is a mango seller if their name ends with 'm'.
    
    BFS ALGORITHM:
    1. Create queue with starting node's neighbors
    2. Create set to track who we've already checked
    3. While queue is not empty:
       a. Pop person from front of queue
       b. If not already checked:
          - If they're a seller, return them!
          - Otherwise, add their neighbors to queue
          - Mark them as checked
    4. Return None if no seller found
    
    WHY TRACK "SEARCHED"?
    - Prevents infinite loops (A → B → A → B → ...)
    - Prevents checking same person twice
    """)
    
    graph = {
        "you": ["alice", "bob", "claire"],
        "bob": ["anuj", "peggy"],
        "alice": ["peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],  # thom ends with 'm' - mango seller!
        "jonny": [],
    }
    
    print("Testing with graph:")
    print("    you → alice, bob, claire")
    print("    claire → thom (ends with 'm' = seller!)")
    print()
    
    try:
        result = search(graph, "you")
        if result == "thom":
            print(f"    search(graph, 'you') = '{result}' ✅")
            print("    Found thom - the mango seller!")
        elif result is None:
            print(f"    search(graph, 'you') = None ❌")
            print("    Should have found 'thom'")
        else:
            print(f"    search(graph, 'you') = '{result}'")
            if result and result[-1] == 'm':
                print(f"    ✅ Found a mango seller!")
            else:
                print(f"    ❌ '{result}' doesn't end with 'm'")
    except Exception as e:
        print(f"    ❌ Error: {e}")


def demo_shortest_path() -> None:
    """Demonstrate shortest path finding."""
    print_header("PART 2: bfs_shortest_path()")
    
    print("""
    Find the shortest path between two nodes.
    
    MODIFICATION TO BFS:
    - Instead of just tracking visited nodes
    - Track the PATH to each node
    - Queue stores: (node, path_to_node)
    
    EXAMPLE:
    Find path from "you" to "peggy"
    
    Paths explored:
    1. you → alice → peggy  (length 2)
    2. you → bob → peggy    (length 2)
    
    BFS finds shortest path first!
    """)
    
    graph = {
        "you": ["alice", "bob"],
        "alice": ["peggy"],
        "bob": ["peggy", "anuj"],
        "peggy": [],
        "anuj": [],
    }
    
    print("Testing shortest path:")
    
    test_cases = [
        ("you", "peggy", ["you", "alice", "peggy"]),  # or ["you", "bob", "peggy"]
        ("you", "anuj", ["you", "bob", "anuj"]),
        ("you", "you", ["you"]),
        ("alice", "anuj", None),  # No path
    ]
    
    for start, end, expected in test_cases:
        try:
            result = bfs_shortest_path(graph, start, end)
            if result is not None and expected is not None:
                # Check if it's a valid path of correct length
                if len(result) == len(expected):
                    print(f"    path('{start}' → '{end}') = {result} ✅")
                else:
                    print(f"    path('{start}' → '{end}') = {result}")
                    print(f"        Expected length {len(expected)}, got {len(result)}")
            elif result is None and expected is None:
                print(f"    path('{start}' → '{end}') = None ✅ (no path exists)")
            else:
                print(f"    path('{start}' → '{end}') = {result} ❌")
        except Exception as e:
            print(f"    path('{start}' → '{end}') ❌ Error: {e}")


def bfs_vs_dfs() -> None:
    """Compare BFS and DFS."""
    print_header("BFS vs DFS")
    
    print("""
    BFS (Breadth-First Search)     DFS (Depth-First Search)
    -------------------------      -------------------------
    Uses: Queue (FIFO)             Uses: Stack (LIFO)
    Explores: Level by level       Explores: Deep first
    Finds: Shortest path           Finds: Any path
    Memory: O(width of tree)       Memory: O(depth of tree)
    
    WHEN TO USE:
    - BFS: Finding shortest path, closest match
    - DFS: Exploring all possibilities, maze solving
    
    VISUALIZATION:
    
    BFS explores like ripples in water:
        1 → 2 → 3 → 4 → 5 → 6 → 7
        
            1
           /|\\
          2 3 4
         /|   |
        5 6   7
    
    DFS explores like following a path:
        1 → 2 → 5 → 6 → 3 → 4 → 7
    """)


def main():
    """Main entry point."""
    print("\n" + "🔍" * 30)
    print("   LAB 06: BREADTH-FIRST SEARCH")
    print("   Finding Shortest Paths!")
    print("🔍" * 30)
    
    print("""
    📋 YOUR TASKS:
    1. Open bfs.py
    2. Implement these functions:
       - search() - Find mango seller
       - bfs_shortest_path() - Find shortest path
    3. Run this file to test: python main.py
    4. Run pytest when ready: python -m pytest tests/ -v
    """)
    
    graph_intro()
    queue_intro()
    demo_mango_seller()
    demo_shortest_path()
    bfs_vs_dfs()
    
    print_header("NEXT STEPS")
    print("""
    When all tests pass, run: python -m pytest tests/ -v
    Then complete the Lab Report in README.md
    """)


if __name__ == "__main__":
    main()
