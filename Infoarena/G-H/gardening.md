# Gardening

Azusa, the witch of the mountains, wants to engage in a fun activity with her friend Laika: gardening. They want to build a rectangular garden of $N$ meters in height and $M$ meters in width. The garden is divided into squares of $1$ meter by $1$ meter. They asked themselves the following question: which flowers should they plant? Laika has $K$ different types of flowers at her disposal. Azusa and Laika will plant one type of flower in each $1$ meter by $1$ meter square. Additionally, for aesthetic reasons, the garden must satisfy the following properties:

- Each type of flower must appear at least once in the garden.
- For any two squares where the same type of flower is planted, there must be a path between them where all intermediate squares have the same type of flower. For example, the following gardens are not allowed:
  
  ~[example1.png]
  
- Any square must have exactly two adjacent squares where the same type of flower is planted. For example, the following gardens are not allowed:
  
  ~[example2.png]

Note that in the above restrictions, two squares are "adjacent" if and only if they share a side (not just a corner); and a path is a sequence of adjacent squares.

You are given $T$ different values for $N$, $M$, and $K$. Help Azusa and Laika create gardens that satisfy the conditions for each test in the input or, if there is no solution, tell them that this is impossible.

## Input data

The first line of input contains the integer number $T$. Next, there are $T$ lines, each describing a test. Each test consists of three integers $N$, $M$, and $K$.

## Output data

Print the answers for each test in order. For a test, if there is no solution, print `NO` on a single line. Otherwise, first print `YES` on a single line, then print $N \times M$ integers arranged on $N$ lines and $M$ columns describing the required garden. The rows and columns in the output correspond to the rows and columns of the garden, each integer representing the type of flower planted in a $1$ meter by $1$ meter square. The types are indexed from $1$ to $K$. If there are multiple correct solutions, you can print any of them.

## Constraints

$1 \leq N, M \leq 200000$. 
$1 \leq K \leq N \times M$. 
Let $S$ be equal to the sum $N \times M$ for all tests in one file for which there is an answer (i.e., for which the displayed answer is not `NO`). 
$S \leq 200000$. 
For $5$ points, $N, M \leq 4$. 
For another $6$ points, $N \leq 4$. 
For another $10$ points, $N \leq 6$. 
For another $18$ points, $N = M$. 
For another $36$ points, $K$ is a number between $1$ and $N \times M$ chosen uniformly at random.

## Examples

`gardening.in`
```
5
2 2 2
2 2 1
4 4 4
4 6 3
2 4 6
```

`gardening.out`
```
NO
YES
1 1
1 1
YES
1 1 2 2
1 1 2 2
3 3 4 4
3 3 4 4
YES
1 1 1 1
1 2 2 1
1 2 2 1
1 1 1 1
YES
1 1 1 1 1 1
1 2 2 3 3 1
1 2 2 3 3 1
1 1 1 1 1 1
```

## Explanations

For the first test case, we notice that no $2$ by $2$ garden with $2$ types of flowers is correct. Therefore, we will print `NO`. The other gardens are illustrated below: