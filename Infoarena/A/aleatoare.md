## Task

The first task is to help $Ymüsnı$ reconstruct the initial matrix. The second task is to respond to $LeCram$ with the maximum lexicographical matrix that $Ymüsnı$ could build in any context. 

## Input data

The input file `aleatoare.in` contains, on the first line, the numbers $C$ (task: can be $1$ or $2$) and $T$ (number of tests). On the following lines, the $T$ tests are described: 

If $C = 1$, first appears the number $N$ and on the next $2N$ lines; Each of these lines describes a sheet, through $N$ numbers each.

If $C = 2$, only the number $N$ appears, because the sheets given by $Marcel$ no longer matter, $LeCram$ can give any sheets he wants. 

## Output data

The output file `aleatoare.out` contains, regardless of the task, $T$ matrices, described through $N$ lines with $N$ numbers each. 

When $C = 1$, the displayed matrix is the one found by $Ymüsnı$ that corresponds to the received sheets. 

When $C = 2$, the displayed matrix is still found by $Ymüsnı$, but in the case where $LeCram$ would give the sheets in such a way that the result is the maximum lexicographical. 

## Constraints and clarifications

$1 \leq T \leq 10$ 

$1 \leq N \leq 50$ 

It is guaranteed that, for the test data, the reconstruction performed by $Ymüsnı$ is possible, meaning there are no errors in the sheets.

For the evaluation, $10$ tests will be used. 

Even-indexed tests will have $C = 2$, while odd-indexed tests will have $C = 1$ 

For the first $2$ tests, we guarantee that $1 \leq N \leq 10$ 

For the next $2$ tests, we guarantee that $11 \leq N \leq 20$ 

For the next $2$ tests, we guarantee that $21 \leq N \leq 30$ 

For the next $2$ tests, we guarantee that $31 \leq N \leq 40$ 

For the last $2$ tests, we guarantee that $41 \leq N \leq 50$ 

## Example

`aleatoare.in`

```
1
2
3
4 9 3
3 5 2
8 2 1
6 7 5
7 4 8
6 1 9
4 3 2
5 9 3
7 6 1
16 8 1
4 13 6
14 10 15
16 10 5
2 14 8
11 13 9
4 12 11
15 12 7
1 2 8
6 5 7
9 3 4
1 3 6
7 4 9
13 12 8
2 14 11
16 5 10
15 2 2
1 1
3 4
2 1
```

`aleatoare.out`

```
3 1
3 2
4 1
2 4
```

## Explanation

In the second example, the first test, $LeCram$ can give the sheets:

```
[3, 1], 
[3, 2],
[4, 1],
[2, 4]
```