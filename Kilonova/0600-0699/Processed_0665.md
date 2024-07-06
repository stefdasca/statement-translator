Anna drew a polygon with $n$ vertices numbered from $0$ to $n - 1$ in a clockwise order. Later, she triangulated the polygon by drawing $n - 3$ diagonals that do not intersect except possibly at the vertices. A diagonal is a straight line between two different vertices that do not have an edge between them.

First, let's define the distance from vertex A to diagonal D. Let's say we start at vertex A and move to the next vertex in the clockwise direction until we reach one of the vertices of D. The number of edges crossed is called **left_distance**. Similarly, **right_distance** is the number of edges crossed if we start from A and move in the counterclockwise direction until we reach D. The distance from A to D is the **maximum** of **left_distance** and **right_distance**.

In the example from the image, the distance from vertex 0 to the diagonal (1, 5) is 2, with left_distance equal to 1 and right_distance equal to 2. For the diagonal (0, 5), the distance from vertex 0 is 5, with left_distance=5 and right_distance=2.

Anna wants to make this a challenge for Jacob. Jacob does not know the drawn diagonals. He only knows the value of $N$, but he can ask Anna several times about pairs of vertices, and she will tell him if there is an edge between those vertices. Jacob's goal is to find the closest (according to the above definition of distance) drawn diagonal to vertex 0. You will help him achieve his goal by asking Anna a limited number of questions.

# Constraints and clarifications

* $5 \leq n \leq 100$

You need to implement the following function in your submission:

```cpp
int solve (int x, int y)
```

* $x$: the index of the first vertex
* $y$: the index of the second vertex
* $0 \leq x, y \leq n - 1$
* If there are multiple diagonals with the same minimum distance, you can return any one of them.

The above function can call the following function:

```cpp
int query (int x, int y)
```

* $x$: the index of the first vertex
* $y$: the index of the second vertex
* $0 \leq x, y \leq n - 1$
* returns 1 if there is a diagonal between $x$ and $y$ and 0 otherwise.

Below is an example of input for the evaluator and the corresponding function calls. The input corresponds to the drawing in the image above.

The single line of input contains $n$.

The evaluator will display each query call to stdout, and you must respond to them manually with $1$ or $0$.

~[triangulationtabel.png]

# Scoring

Let $q$ be the number of queries you make in a single test. Let $w = \frac{n ( n - 3)}{2}$.

* If you make an invalid query or guess the answer incorrectly, you will receive $0\%$ of the points.
* If $w < q$ you will receive $0\%$ of the points for the test.
* If $n < q \leq w$ you will receive $10 + 60 \cdot \frac{w - q}{w - n} \%$ of the points for a test.
* If $q \leq n$ you will receive $100 \%$ of the points for the test.