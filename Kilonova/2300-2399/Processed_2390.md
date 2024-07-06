```markdown
Let's consider sequences of undirected graphs of the following types:
* Type $A$
The sequence of type $A$ graphs is constructed in a way that can be deduced from the following examples:
~[img1.png]
Notice that the graph $A_n$ has $2n$ vertices.
* Type $B$
The sequence of type $B$ graphs is constructed according to the following model:
~[img2.png]
* Type $C$
The sequence of type $C$ graphs is constructed according to the following model:
~[img3.png]

A perfect matching in a graph is a way of choosing edges of the graph such that any vertex in the graph is incident to exactly one chosen edge. Two matchings are distinct if there exists an edge that belongs to one matching but does not belong to the other.

# Task
Given a graph of one of the types mentioned, determine the number of distinct perfect matchings of the respective graph.

# Input data 
The input file `perfect.in` contains a single line that contains a character and a non-zero natural number $n$, separated by a space. The character can be $A, B$, or $C$ and indicates the type of the graph. The natural number $n$ indicates the order number of the graph in the sequence of graphs of the specified type.

# Output data
The output file `perfect.out` will contain a single line that will contain the number of perfect matchings of the graph from the input file.

# Constraints and clarifications

* $1 \leq n \leq 100$ 

# Example 1

`perfect.in`
```
A 4
```

`perfect.out`
```
5
```

## Explanation

The $5$ perfect matchings of the graph $A4$ are:
~[img4.png]

# Example 2

`perfect.in`
```
B 2
```

`perfect.out`
```
4
```

## Explanation

The $4$ perfect matchings of the graph $B2$ are:
~[img5.png]

# Example 3

`perfect.in`
```
C 2
```

`perfect.out`
```
8
```

## Explanation

The $8$ perfect matchings of the graph $C2$ are:
~[img6.png]
```