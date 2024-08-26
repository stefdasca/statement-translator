## Task

Alexandra is a student at the Faculty of Computer Science. Today, while walking back home, she noticed that on the street there are $N$ small posts placed along the edge of the sidewalk. Being a computer science student, she immediately thinks of a computer science problem based on this observation. She wonders what the minimum distance $D$ is, such that for each of the $N$ posts, in the interval $[P_i - D, P_i + D]$ there are at least $K$ posts, where $P_i$ represents the distance from the beginning of the street to post $i$. Given that Alexandra failed her algorithms exam, she is asking you to help her solve this problem.

## Input data

The input file `stalpisori.in` contains on the first line 2 numbers, $N$ and $K$. The next $N$ lines contain the distances from the beginning of the street to each post.

## Output data

The output file `stalpisori.out` will contain a single number representing the minimum distance required as stated in the problem.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$1 \leq K \leq N$

The positions of the posts are distinct natural numbers strictly less than $2^{31}$.

The positions of the posts will be given in ascending order.

## Example

`stalpisori.in`

```
10 3
5
9
14
20
24
26
35
38
41
43
```

`stalpisori.out`

```
9
```