## Task

Tanaka has decided to go to the NicioMare festival, held in the magical land of Tomisului. He now has to decide which DJs to attend. At NicioMare, there will be $N$ DJs, with the $i$-th DJ having a value index of $v_i$. Tanaka will watch at most $K$ disjoint subarrays of DJs. Unfortunately, if the total value of a subarray he watches becomes too high, Tanaka wouldn't be able to properly appreciate the greatness of the DJs. Thus, each watched subarray must have a sum of indices of values at most $S$. Tanaka wants to have as much fun as possible at the festival. As we all know, you have more fun if you see two super cool DJs one after the other rather than taking a break between them. Therefore, Tanaka realizes that if he watches a subarray of DJs that has a sum of indices of values equal to $X$, then that subarray will contribute $X^2$ to his total fun. Help Tanaka select which subarrays of DJs to watch so that his total fun is maximized. In other words, select at most $K$ disjoint subarrays from array $v$ (which do not necessarily need to cover the entire array), such that each subarray has a sum of at most $S$, and the sum of the squares of the sums of the subarrays is as large as possible.

## Input data

The input file `niciomare.in` will contain, on the first line, the values $N$, $K$, $S$. The second line will contain the values of the array $v$, in order.

## Output data

The output file `niciomare.out` will print the required value.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq K \leq 100$

$1 \leq S \leq 100000000$

$1 \leq v_i \leq S$

For 30 points,

$N \leq 1000$

$K \leq 10$

feedback tests 1, 4.

For another 30 points,

$N \leq 100000$

$N * K \leq 100000$

feedback tests 10, 15.

For another 10 points,

$N \leq 100000$

$N * K \leq 1000000$

feedback tests 19, 20.

The rest of the feedback tests are part of the largest tests.

## Example

`niciomare.in`

10 2 5

1 2 3 4 1 2 3 4 1 2

`niciomare.out`

50

`niciomare.in`

10 5 91

3 8 4 2 3 1 1 5 8 3

`niciomare.out`

1444

`niciomare.in`

10 4 91

6 3 1 3 4 8 8 4 4 2

`niciomare.out`

1849

`niciomare.in`

10 4 97

6 3 4 6 6 7 2 2 2 8

`niciomare.out`

2116

`niciomare.in`

10 5 94

5 5 8 7 2 1 4 1 4 6

`niciomare.out`

1849

`niciomare.in`

100 5 98

3 7 8 5 6 4 2 8 2 6 5 2 5 5 6 5 2 3 2 3 1 2 1 2 7 6 8 4 4 7 7 1 5 1 6 8 1 3 4 5 2 2 4 8 6 1 8 1 4 2 2 8 8 7 7 1 3 3 3 3 4 7 5 6 4 1 3 8 4 8 6 2 7 5 4 8 8 5 8 8 8 6 4 7 8 3 3 4 7 3 3 3 8 8 2 2 2 1 4 2

`niciomare.out`

41658

`niciomare.in`

100 6 99

2 6 6 4 8 5 3 4 88 4 2 7 8 5 6 6 8 7 7 8 7 1 8 6 4 1 8 1 5 4 1 3 6 1 3 1 5 4 4 7 1 6 1 1 5 2 1 2 26 6 1 6 4 8 8 2 2 4 5 8 8 3 6 8 2 8 3 7 1 6 3 4 2 6 3 5 5 5 7 1 1 1 31 6 4 1 3 1 7 2 1 7 8 1 4 4 3 2 4 1

`niciomare.out`

49966

`niciomare.in`

100 8 95

2 3 1 7 5 7 2 3 3 4 6 4 6 5 8 6 3 6 1 1 7 1 8 1 6 4 1 2 7 7 6 7 3 7 2 7 6 5 1 6 5 8 8 3 5 6 5 5 3 7 3 3 5 4 8 7 8 4 4 7 5 4 4 8 6 2 6 8 6 4 3 1 4 3 3 5 4 7 8 6 3 4 6 6 5 4 1 8 5 5 3 6 8 8 2 7 5 7 7 1

`niciomare.out`

44621

`niciomare.in`

100 10 96

1 6 8 2 8 96 7 1 5 8 3 5 3 1 7 2 5 27 4 4 6 4 4 6 4 8 5 7 4 2 8 3 3 1 7 3 6 5 1 8 3 1 7 8 4 6 4 3 1 6 5 2 3 6 8 3 4 2 1 6 8 3 3 5 8 2 1 7 8 3 6 1 6 8 6 1 6 3 7 2 5 5 7 5 3 1 1 4 4 4 7 3 5 4 8 5 4

`niciomare.out`

57342

## Explanation

To fit better on the page, the large examples (with $N = 100$) have the second line split into several parts; the true input files will have them on a single line.