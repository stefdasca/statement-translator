
# Task

Adrian Wonder Boy has just received a new game. It consists of $n$ equilateral triangles placed in a vertical plane with one horizontal side and the opposite vertex pointing upwards. The triangles have side lengths of $1, 2, 3, \dots, n$ and are nested within each other so that any two consecutive triangles share a common angle. More precisely, a small triangle (of side $i$; in the drawing $i=3$) can be in exactly the following $3$ positions relative to the larger triangle (of side $i+1$):

~[lru.png]

The state of the game at any moment can be encoded by a string of $n-1$ characters `L`, `R`, or `U` describing the position of each triangle of side $i$ relative to the triangle of side $i+1$. For example, for $n=4$ in the figures below, we have three states of the game along with their encodings.

~[lru2.png]

The state of the game can be modified by sliding one of the inner triangles along the direction of one of the edges, in either direction, by exactly one unit. For instance, sliding the triangle of side $2$ horizontally to the right can change from state $2$ to state $3$. Relative to the triangle of side $3$, the triangle of side $2$ has moved from left to right. (Note that sliding a triangle leaves the inner triangles in their old positions, so some moves are not possible. For example, in state $1$, the triangle of side $2$ cannot slide upward because the triangle of side $1$ would be left outside the triangle of side $2$.)

For several tests, given $n$ and two states of the game, determine the minimum number of slides required to transform the game from the first state to the second state.

# Input data

The file `lru.in` will contain a natural number $t$ - the number of tests. The next $3 \cdot t$ lines describe the $t$ tests, one test on each $3$ lines. The first line of the $3$ contains a natural number $n$ – the common length of the encoding of the two states. The second line of the $3$ contains a string of $n$ characters – the encoding of the initial state. The third line of the $3$ contains a string of $n$ characters – the encoding of the final state.

# Output data

The file `lru.out` will contain $t$ lines. Line $k \ (1 \leq k \leq t)$ will contain a natural number $m_k$ – the solution of test $k$ from the input file.

# Constraints and clarifications

* $1 \leq t \leq 5$
* $2 \leq n \leq 1 \ 000 \ 000$
* For $70\%$ of the tests, $n \leq 200 \ 000$

# Example

`lru.in`
```
1
3
RLL
LRU
```

`lru.out`
```
5
```

## Explanation

There are $5$ slides and the game goes through the following states:
RLL $ \rightarrow $ ULL $ \rightarrow $ LUL $ \rightarrow $ RUL $ \rightarrow $ RLU $ \rightarrow $ LRU
```
