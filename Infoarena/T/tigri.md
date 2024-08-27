## Task

Marcel needs your help! He sends you $N$ operations that he would like you to perform, in order, on his account. The operations are of three types:
- `depositum $X$`, where $X$ is an integer: Deposit $X$ lei into Marcel's account.
- `emptum $X$ $Y$`, where $X$ and $Y$ are integers, and $Y$ is non-zero: Buy $X$ tigers at the price of $Y$ lei per tiger.
- `vendere $X$ $Y$`, where $X$ and $Y$ are integers, and $Y$ is non-zero: Sell $X$ tigers at the price of $Y$ lei per tiger.

You will perform each operation either completely - if neither the number of lei nor the number of tigers Marcel has would become negative - or not at all. After each operation, whether performed or not, display the number of lei in Marcel's account. It is guaranteed that this number can be represented in the `int` type of C/C++. Initially, Marcel's account contains no lei and no tigers.

## Input data

The input file `tigri.in` contains the number $N$ in the first line, and in the following $N$ lines, a string of up to $99$ characters describing an operation.

## Output data

The output file `tigri.out` contains $N$ numbers separated by a space, representing the number of lei in Marcel's account, as it is after each operation, whether performed or not.

## Constraints and clarifications

$1 \leq N \leq 100000$

The number of characters in the input file does not exceed $2000000$ 

## Example

`tigri.in`

```
6
depositum 9
emptum 3 2
vendere 4 10
depositum 15
emptum 10 2
emptum 6 3
```

`tigri.out`

```
9 3 3 18 18 0
```

`tigri.in`

```
12
depositum 100
emptum 100 1
depositum 9
emptum -3 -2
vendere -4 -10
depositum 15
emptum -10 -2
emptum -6 -3
vendere 0 12345678900987654321
depositum -10000000000000000000000000000000000
emptum -100000000000000000000000000000 -1000000000000000000000000
vendere -100000000000000000000000000000000 10000000000000000000000000000000
```

`tigri.out`

```
100 0 9 9 9 24 24 24 24 24 24 24
```