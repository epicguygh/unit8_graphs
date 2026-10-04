"""
============================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
============================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

============================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the starting node does not exist, return an empty traversal.
    if start not in graph:
        return []

    # BFS uses a queue because it follows FIFO (first-in, first-out)
    # behavior. This allows nodes to be explored level by level.
    queue = deque([start])

    # The visited set prevents the same node from being processed
    # more than once, especially when nodes have multiple connections.
    visited = {start}

    # This list stores the order in which nodes are visited.
    traversal_order = []

    while queue:
        # Remove the first node that was added to the queue.
        current = queue.popleft()

        # Record the node in the order it was visited.
        traversal_order.append(current)

        # Add each unvisited neighbor to the queue.
        # Neighbors are queued so that they are explored after
        # the nodes already waiting in the queue.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ==========================================
    # TODO (Student): CREATE A GRAPH
    # ==========================================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    # The graph represents locations in a small community.
    # Each key is a location/node, and its list contains
    # locations directly connected to that node.
    graph = {
        "Home": ["School", "Library"],
        "School": ["Home", "Gym", "Cafeteria"],
        "Library": ["Home", "Cafeteria"],
        "Gym": ["School", "Cafeteria"],
        "Cafeteria": ["School", "Library", "Gym"],
        "Park": ["Cafeteria"]
    }

    print("\n=== GRAPH STRUCTURE ===")

    # Display the adjacency-list representation of the graph.
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # ==========================================
    # TODO (Student): BFS TRAVERSAL
    # ==========================================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start_node = "Home"
    traversal = bfs(graph, start_node)

    print(f"Starting node: {start_node}")
    print(f"BFS traversal: {traversal}")

    print("\nBFS explanation:")
    print("BFS starts at Home and first visits its immediate neighbors.")
    print("It then processes the next level of connected nodes.")
    print("The queue maintains FIFO order so nodes are visited level by level.")

    # Add an additional node and edge to demonstrate an updated graph.
    # The new location "Hospital" is connected to the Park.
    graph["Hospital"] = ["Park"]
    graph["Park"].append("Hospital")

    print("\n=== UPDATED GRAPH ===")

    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    # Demonstrate the updated traversal.
    updated_traversal = bfs(graph, "Home")

    print("\nUpdated BFS traversal from Home:")
    print(updated_traversal)

    # ==========================================
    # TODO (Student): EDGE CASES
    # ==========================================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1:
    # Start BFS from a different node.
    # BFS should begin at Park and visit nodes reachable from Park.
    different_start = "Park"
    result_different_start = bfs(graph, different_start)

    print(f"Edge Case 1 - Starting from {different_start}:")
    print(result_different_start)

    # Edge Case 2:
    # Use a start node that does not exist in the graph.
    # The BFS function safely returns an empty list instead of
    # producing an error.
    missing_node = "Airport"
    result_missing_node = bfs(graph, missing_node)

    print(f"\nEdge Case 2 - Missing start node ({missing_node}):")
    print(result_missing_node)

    # Edge Case 3:
    # Test a disconnected graph.
    # The node "Museum" is not connected to the other nodes.
    disconnected_graph = {
        "A": ["B"],
        "B": ["A"],
        "C": []
    }

    disconnected_result = bfs(disconnected_graph, "A")

    print("\nEdge Case 3 - Disconnected graph:")
    print(f"Graph: {disconnected_graph}")
    print(f"BFS starting at A: {disconnected_result}")

    print(
        "Explanation: BFS only visits nodes reachable from the starting node."
    )


if __name__ == "__main__":
    main()