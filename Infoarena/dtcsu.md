## Task

You are given all the numbers of the form $2^a 3^b 5^c 7^d 11^e$ $(a, b, c, d, e$ are natural numbers$)$ from the interval $[0, 10^{18}]$, followed by $Q$ queries in the form: Can $N$ be written as $2^w 3^x 5^y 7^z 11^t$ where $w, x, y, z, t$ are natural numbers?

## Input data

The input file `dtcsu.in` contains on the first $276997$ lines all the numbers of the mentioned form. It then contains on a new line the natural number $Q$ representing the number of queries, followed by $Q$ lines each containing a value $N$ which you need to verify.

## Output data

The output file `dtcsu.out` contains on a single line the number of values of $N$ that satisfy the task.

## Constraints and clarifications

$1 \leq Q \leq 5000000$
$0 \leq N \leq 10^{18}$
The total number of solutions represents approximately $20\%$ of the total number of queries.
It is recommended to parse the reading (reading a full line as a string using `fgets` followed by converting the string to a number; this technique can improve execution time when the input is very large, given that IO calls on a magnetic hard drive are quite expensive).

## Example

`dtcsu.in`
```
...(276997 lines)
3
1
13
10
```

`dtcsu.out`
```
2
```

## Explanation

$1 = 2^0 3^0 5^0 7^0 11^0$

$10 = 2 * 5$