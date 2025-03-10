
# Task

In the peculiar city of Little Gates, the town hall has installed $n$ lamp posts on a street, arranged in a line, at equal distances of $1$ meter between them. Each post is uniquely identified by its position in the sequence, from $1$ to $n$. The first lamp post is at position $1$ (at the beginning of the street), the second lamp post at position $2$, and so on, until position $n$, where the last lamp post is located (where the street ends). The peculiarity lies in the fact that the lamp posts have different heights, with each post providing illumination in the area it is located at, over a distance equal to its height on both the left and the right. For example, if a lamp post has a height of $x$, it will ensure illumination over a distance equal to $x$ meters to the left and $x$ meters to the right (including its own position). The height of each lamp post is known.

Little Gates receives from the town hall the task of answering the following questions:
1. What is the largest height difference between two consecutive lamp posts in the sequence?
2. What is the minimum number of lamp posts that must be kept in order for the street to be completely illuminated?

## Input data

The input file `stalpi.in` contains:
- on the first line a value $1$ or $2$ representing the number of the task that needs to be solved;
- on the second line an integer $n$, representing the number of lamp posts;
- on the third line $n$ non-zero natural numbers separated by a space, where the $i$-th number represents the height of the lamp post at position $i$.

## Output data

The first line of the output file `stalpi.out` will contain a single number representing the answer in accordance with the task that needs to be solved.

## Constraints and clarifications

* $2 \leq n \leq 10^6$;
* For task $1$, $32$ points are granted;
* For task $2$, $68$ points are granted. Out of these, for $24$ points, $n \leq 10^3$;
* For all tests, $1 \leq h_i \leq 10^3$ for any $i$ between $1$ and $n$.

## Example 1
`stalpi.in`
```
1
3
5 10 8
```

`stalpi.out`
```
5
```
## Explanation
The maximum difference between two neighboring lamp posts is 5 (between post 1 and post 2).

## Example 2
`stalpi.in`
```
2
10  
1 2 1 1 3 1 2 1 1 1  
```
`stalpi.out`
```
3
```

## Explanation
The smallest number of lamp posts needed is 3. 
$1 \ \mathbf{2} \ 1 \ 1 \ \mathbf{3} \ 1 \ 2 \ 1 \ 1 \ \mathbf{1}$ (the post at position 2, the one at position 5, and the one at position 10)

## Example 3

`stalpi.in`
```
2
10
1 1 1 1 1 1 1 1 1 1
```

`stalpi.out`
```
4
```

## Explanation

$1 \ \mathbf{1} \ 1 \ 1 \ \mathbf{1} \ 1 \ 1 \ \mathbf{1} \ 1 \ \mathbf{1}$. We need 4 posts.
The first chosen post covers positions from $1$ to $3$, inclusive.
The second chosen post covers positions from $4$ to $6$, inclusive.
The third chosen post covers positions from $7$ to $9$, inclusive.
The fourth chosen post covers positions from $9$ to $10$, inclusive.
