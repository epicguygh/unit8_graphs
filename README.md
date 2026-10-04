# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

Reflection

Completing this assignment helped me understand how graphs can be represented using adjacency lists and how Breadth-First Search (BFS) can be used to traverse connected nodes. I learned that BFS uses a queue to maintain a first-in, first-out (FIFO) order. When a node is visited, its unvisited neighbors are added to the queue, allowing BFS to explore the graph level by level. I also learned the importance of tracking visited nodes to prevent the program from repeatedly visiting the same nodes.
One challenge I encountered was making sure the traversal handled different situations correctly, such as starting from a different node, using a missing starting node, and working with a disconnected graph. I overcame these challenges by testing multiple starting points and verifying the output against the graph structure.
BFS and Depth-First Search (DFS) both traverse graphs, but they explore nodes differently. BFS explores neighboring nodes first, making it useful for finding the shortest path in an unweighted network. For example, BFS can be used in GPS routing or social networks to find nearby connections. DFS explores one path as deeply as possible before backtracking, which can be useful for maze solving, file systems, and dependency analysis. Overall, this assignment showed me that the best traversal method depends on the problem being solved.