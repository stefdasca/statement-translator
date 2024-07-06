Certainly! Here is the translated statement:

---

A tournament graph with $n$ vertices is considered. We call a _tournament graph_ a directed graph where between any two vertices there is an arc and only one.

# Task:

Find an arrangement of the graph's arcs so that between any two nodes there exists a path of length $1$ or $2$.

# Input data

The input file `graf.in` contains on the first line the value of $n$.

# Output data

The output will be written in the file `graf.out` which contains:

- the adjacency matrix of the graph that meets the problem's requirements (on line $i$ of the file will be line $i$ of the matrix) in case there is a solution;
- the text `fără solutie` (in lowercase letters!), if there is no arrangement of the arcs.

# Constraints and clarifications

* $2 \leq n \leq 250$;

# Example

`graf.in`
```
6
```

`graf.out`
```
0 1 1 1 0 0
0 0 1 1 1 0
0 0 0 1 0 1
0 0 0 0 1 1
1 0 1 0 0 1
1 1 0 0 0 0
```

# Explanations:

The adjacency matrix corresponds to the graph in the image below:

~[graf.png]

---

I have ensured that the translation is accurate and conforms to the specified format instructions. If there are any further corrections or adjustments needed, please let me know.