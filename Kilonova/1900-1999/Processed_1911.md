> "Even when you think they've done the tests properly at joingraf..."

# Task

After the joingraph problem tests were indeed done at the last [RoAlgo](https://discord.gg/roalgo) contest, the committee realized that a special problem was still needed. Thus, after lengthy discussions, the following problem was reached:

Given $t$ arrays $a$ of $n$ numbers, find the length of the longest subarray containing at most $3$ distinct numbers. An example of such a subarray is: $9 \\ 1 \\ 0$.

# Input data

The first line contains the number $t$. For each test, the first line will contain $n$, representing the number of numbers. The second line will contain the $n$ numbers.

# Output data 

The first line contains the maximum length of a subarray with at most $3$ distinct numbers.

# Constraints and clarifications

* $1 \leq t \leq 1 \\ 000$;
* $1 \leq n \leq 10^6$
* The sum of the lengths of the $t$ arrays does not exceed $10^6$.
* $1 \leq a_i \leq 10^9$

|#|Score|Constraints|
|-|--|------------|
|1|0|Example|
|2|14|$1 \leq n \leq 100$|
|3|22|$1 \leq n \leq 5 \\ 000$|
|4|38|$1 \leq n \leq 100 \\ 000$|
|5|26|No additional constraints|

# Example

`stdin`
```
5
10
1 4 7 4 2 4 7 3 2 3 
8
1 2 4 1 5 3 1 2
10
6 8 9 1 8 5 4 6 3 2
6
1 1 1 2 2 2
12
1 5 8 3 2 5 7 4 9 5 7 4
```

`stdout`
```
6
4
4
6
3
```

## Explanation

The subarray `4 7 4 2 4 7` contains $3$ distinct numbers. There is no subarray of length greater than $6$.
