from typing import Dict, List, Optional, Set


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    visited: Set[str] = set()
    on_path: Set[str] = set()

    def dfs(course: str) -> bool:
        # A back edge means we found a cycle.
        if course in on_path:
            return True

        # Already fully explored: no new cycle from this vertex.
        if course in visited:
            return False

        visited.add(course)
        on_path.add(course)

        # Explore all dependent courses.
        for neighbor in graph.get(course, []):
            if dfs(neighbor):
                return True

        # Base case: all neighbors have been explored.
        on_path.remove(course)
        return False

    # Check every component, including disconnected courses.
    for course in graph:
        if dfs(course):
            return True

    return False


def topological_sort(
    graph: Dict[str, List[str]]
) -> Optional[List[str]]:

    # A graph with a cycle cannot have a topological ordering.
    if has_cycle(graph):
        return None

    visited: Set[str] = set()
    finish_order: List[str] = []

    def dfs(course: str) -> None:
        # Base case: already explored.
        if course in visited:
            return

        visited.add(course)

        # Explore all outgoing edges.
        for neighbor in graph.get(course, []):
            dfs(neighbor)

        # Record the vertex after all recursive calls finish.
        finish_order.append(course)

    # Process all vertices, including disconnected components.
    for course in graph:
        dfs(course)

    # Reverse finish order to get a topological order.
    finish_order.reverse()

    return finish_order