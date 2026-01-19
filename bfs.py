"""
Lab 06: Breadth-First Search
Implement BFS from Chapter 6.

BFS answers two questions:
1. Is there a path from A to B?
2. What is the shortest path from A to B?
"""
from typing import List, Dict, Optional
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
    
    Example:
        >>> graph = {"you": ["alice", "bob"], "bob": ["tom"], ...}
        >>> search(graph, "you")
        'tom'
    """
    # TODO: Implement BFS search
    # 1. Create search_queue with start's neighbors
    # 2. Create searched set to track visited
    # 3. While queue not empty:
    #    a. Pop person from front
    #    b. If not searched:
    #       - If person_is_seller, return person
    #       - Else add their neighbors to queue
    #       - Mark as searched
    # 4. Return None if not found
    
    pass


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
    # TODO: Implement BFS shortest path
    # 1. Queue stores (node, path_to_node)
    # 2. Track visited nodes
    # 3. When we reach end, return the path
    
    pass
