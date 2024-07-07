**"Been […] confused for so long it's not true"**

ZLed has become a bit confused lately, so he started playing with trees (for therapeutic purposes). Each node in the tree can be colored either white or black. Initially, all nodes are colored white.

During the game, ZLed can choose a node in the tree to change its color (from white to black or from black to white). Also, he can select two nodes `x` and `y` in the tree, with `x` being an ancestor of `y`, and he can ask: *"Of all the nodes on the path from `x` to `y` (including `x` and `y`), which is the closest node to `x` that is colored black?"*.

# Task
Because you want to dissipate ZLed's confusion, you need to help him and resolve the operations of coloring a node, and querying the closest node colored black on the path from `x` to `y`, for an ancestor `x` of `y`.

# Input data
The file `confuzie.in` will contain on the first line two numbers `N` and `M`, where `N` is the number of nodes in the tree, and `M` is the number of operations to be performed, both color changes and queries.

The next `N-1` lines contain a description of the tree, with each line containing two numbers `a` and `b`, signifying that there is an edge between `a` and `b` in the tree.

The next `M` lines describe the operations to be performed. The first number on each of these lines represents the type of operation: `0` if it is a color change, and `1` if it is a query. In the first case, after `0` there will follow a number `x`, signifying that the color of `x` will be changed from black to white or from white to black. In the second case, after `1` there will follow two numbers `x` and `y`, with `x` being an ancestor of `y`, signifying that we want to find, among all the nodes on the path from `x` to `y`, the closest node to `x` that is colored black.

# Output data
The file `confuzie.out` will contain one line for each query operation present in the input file. This line can contain either the required node (the closest black node to `x` on the path between the two given nodes in the query), or `-1` if the path between the given nodes in the query contains no nodes colored black.

# Constraints and clarifications:
* The root of the tree is considered to be the node with index `1`.
* `1 \leq N \leq 200000`
* `1 \leq M \leq 450000`
* `1 \leq x, y, a, b \leq N`
* A *tree* is an undirected, connected, and acyclic graph.
* A node `x` is called an *ancestor* of `y` if it is on the path from `y` to the root of the tree.

# Example:

`confuzie.in`  
```
7 10
1 2
2 4
1 3
3 5
4 6
3 7
0 2
1 1 2
1 1 1
0 1
1 1 2
0 5
1 3 5
1 3 7
0 1
1 1 5
```

`confuzie.out`
```
2
-1
1
5
-1
5
```

Explanations
---

Step-by-step operations:

Set `2` to black  
From the path `[1, 2]`, `2` is black  
From the path `[1, 1]`, there is no black node  

Set `1` to black  
From the path `[1, 2]`, `1` and `2` are black, the first is `1`  

Set `5` to black  
From the path `[3, 5]`, `5` is black  
From the path `[3, 7]`, there is no black node  

Set `1` to white  
From the path `[1, 3, 5]`, `5` is black