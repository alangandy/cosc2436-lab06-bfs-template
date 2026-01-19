"""Lab 06: Test Cases for BFS"""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bfs import search, bfs_shortest_path, person_is_seller


# Graph from Chapter 6
GRAPH = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


class TestPersonIsSeller:
    def test_is_seller(self):
        assert person_is_seller("thom") == True
    
    def test_not_seller(self):
        assert person_is_seller("alice") == False


class TestSearch:
    def test_find_seller(self):
        result = search(GRAPH, "you")
        assert result == "thom"  # thom ends with 'm'
    
    def test_no_seller(self):
        graph = {"you": ["alice", "bob"], "alice": [], "bob": []}
        result = search(graph, "you")
        assert result is None


class TestBFSShortestPath:
    def test_direct_path(self):
        path = bfs_shortest_path(GRAPH, "you", "bob")
        assert path == ["you", "bob"]
    
    def test_two_hop_path(self):
        path = bfs_shortest_path(GRAPH, "you", "thom")
        assert path == ["you", "claire", "thom"]
    
    def test_no_path(self):
        graph = {"a": ["b"], "b": [], "c": []}
        path = bfs_shortest_path(graph, "a", "c")
        assert path is None
    
    def test_same_node(self):
        path = bfs_shortest_path(GRAPH, "you", "you")
        assert path == ["you"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
