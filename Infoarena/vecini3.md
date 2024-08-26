# Vecini3

We are in the year 2030, and the pandemic is finally over, so the students have returned to school. In gym class, there are $N$ children numbered with natural numbers from $1$ to $N$. Initially, they are arranged in a straight line in a certain order. The children's arrangement can be viewed as a permutation $A$ of the numbers from $1$ to $N$. The children play a game where they are allowed to perform the following $2$ types of operations: The neighbors of the child in position $i$ swap places ($1 < i < number$ of remaining children in the game). The neighbors of the child in position $i$ are eliminated from the game ($1 < i < number$ of remaining children in the game). Although one of the operations involves eliminating two children, this game is not about a single winner but about teamwork. Thus, the gym teacher asks the children to cooperate and, starting from the initial configuration $A$ and using the two types of operations, reach a final configuration $B$. The final configuration $B$ consists of a subset of $M$ children ($M \leq N$) of all $N$ children arranged in a straight line in a certain order. It is guaranteed that $N$ and $M$ have the same parity. The children are a bit confused and would first like to know if it is even possible to get from the initial configuration $A$ to the final configuration $B$. Could you help them answer this question?

## Input data

The first line of the input file `vecini3.in` contains the number $T$ of tests in the input. Next are the $T$ tests. Each test contains on the first line the natural numbers $N$ and $M$. The second line of each test contains $N$ numbers representing the initial configuration $A$. The third line of each test contains $M$ numbers representing the final configuration $B$. The array $A$ is a permutation of the numbers from $1$ to $N$, and the array $B$ consists of $M$ distinct numbers with values ranging between $1$ and $N$.

## Output data

The output file `vecini3.out` will contain the answer for the $T$ tests on separate lines. If it is possible to get from the initial configuration to the final configuration, then print $1$, otherwise print $0$.

## Constraints and clarifications

$$
2 \leq M \leq N
$$
The sum of $N$s of the $T$ tests is $\leq 10^6$

$N$ and $M$ have the same parity

### Subtasks

Subtask 1 (10 points)

$N = M$ in all $T$ tests of the file

$$
T \leq 10
$$
$$
2 \leq N \leq 8
$$

Subtask 2 (20 points)

$N = M$ in all $T$ tests of the file

Subtask 3 (20 points)

$$
T \leq 10
$$
$$
2 \leq N \leq 8
$$

Subtask 4 (50 points) No additional constraints

## Example

`vecini3.in`

    4
    5 5
    3 1 4 2 5
    5 2 3 1 4
    4 4
    3 2 4 1
    1 2 4 3
    6 4
    1 6 4 3 2 5
    6 3 4 5
    5 3
    4 2 3 1 5
    2 4 1

`vecini3.out`

    1
    0
    1
    0

## Explanation

In the first test, the children can perform the following operations:

$[3, 1, 4, 2, 5] → $ swap neighbors of $2 → [3, 1, 5, 2, 4] → $ swap neighbors of $1 → [5, 1, 3, 2, 4] → $ swap neighbors of $3 → [5, 2, 3, 1, 4]$

In the second test, it is not possible to obtain $[1, 2, 4, 3]$ starting from $[3, 2, 4, 1]$.

In the third test, the children can perform the following operations:

$[1, 6, 4, 3, 2, 5] → $ swap neighbors of $3 → [1, 6, 2, 3, 4, 5] → $ eliminate neighbors of $6 → [6, 3, 4, 5]$.

In the fourth test, it is not possible to obtain $[2, 4, 1]$ starting from $[4, 2, 3, 1, 5]$.