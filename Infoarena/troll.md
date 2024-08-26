## Task

The troll has an urgent problem. He has several intervals, each with a certain assigned value, and he doesn't know what to do with them. Shortly, he got an idea. What if he picks an interval of maximum value and sees how many more non-overlapping intervals he can add such that they do not overlap at any point. Suddenly, he realizes that he wants to know the maximum value that can be obtained from the above question; unfortunately, he ran out of food and asks you to answer for him. An interval is defined by: the left endpoint $x$, the right endpoint $y$, and the value $z$.

## Input data

The input file `troll.in` will contain on the first line a number $N$, and on the next $N$ lines the $N$ intervals in the form $x$, $y$, $z$ as described above.

## Output data

In the output file `troll.out` you will write two numbers separated by a space. The first number is the maximum value of an interval, and the second number is the maximum number of non-overlapping intervals such that one of them has the maximum value.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq X , Y \leq 2000800000$

$-1337 \leq Z \leq 2000800000$

The time intervals are of the form: $[ x , y ]$

If you do not feed the troll, you will not get 100 points

## Example

`troll.in`
```
2 
1 1 1 
1 1 2
```

`troll.out`
```
2 1
```

## Explanation

The troll can take only one interval, having the value 2.