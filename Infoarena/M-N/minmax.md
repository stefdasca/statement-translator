## Task

You have an array $v$ of $n$ natural numbers. You are planning to divide it into $k$ subsequences, so that each element of the array appears in exactly one subsequence, and the sum of the values of these subsequences is maximized. The value of a subsequence is represented by the difference between the maximum and minimum values of that subsequence. Since the problem doesn't seem difficult enough to you, you want to find the answer for all values of $k$ from $1$ to $n$. A subsequence is a sequence obtained from the initial array by deleting $0$ or more elements, not necessarily consecutive.

## Input data

The input file `minmax.in` contains on the first line a number $n$, and the second line contains $n$ numbers $v[i]$. 

## Output data

The output file `minmax.out` contains $n$ lines, the $k$-th line contains the answer for a division into $k$ subsequences. 

## Constraints

$1 \leq n \leq 100\ 000$

$1 \leq v[i] \leq 1\ 000\ 000\ 000$

The tests are grouped!

Each of the following sets of tests represents a group.

The rest of the tests (those that do not comply with other conditions than the initial ones) are also grouped.

For the first 4 groups, the numbers in the array $v$ are distinct.

For 10 points

$1 \leq n \leq 5$

For another 10 points,

$1 \leq n \leq 10$

For another 10 points

$1 \leq n \leq 100$

For another 10 points

$1 \leq n \leq 1\ 000$

## Example

`minmax.in`

`
4
1 2 3 4
`

`minmax.out`

`
3
4
3
0
`

`minmax.in`

`
3
1 2 1
`

`minmax.out`

`
1
1
0
`

## Explanation

In the first example, we will have the following partitions (as values) in turn: { {1, 2, 3, 4} }, { {1, 4}, {2, 3} }, { {1, 4}, {2}, {3} }, { {1}, {2}, {3}, {4} }.

In the second example, we will have the following partitions (as values) in turn: { {1, 2, 1} }, { {1, 2}, {1} }, { {1}, {2}, {1} }.

Note: The time limit is different from the one during the contest to allow obtaining the maximum score through submissions in Java.