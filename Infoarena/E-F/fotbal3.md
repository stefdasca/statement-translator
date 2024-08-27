## Task

Professional footballer Bossanip decided to play some recreational football with his group of $N$ friends, each equipped with a distinct value different from any other friend's value. First, the $N$ friends line up from $1$ to $N$, and then Bossanip will choose the opposing team, consisting of any compact interval of his friends. As we all know, in football, as in life, the unity of the team matters, absence of divisions between the strong and the weak -- and Bossanip wants the opposing team to be easy to defeat. Thus, help Bossanip count how many teams he could select where the value of the member with the smallest value divides the value of the member with the largest value.

## Input data

The input file `fotbal3.in` will contain, on the first line, the number $N$  
The second line will contain the values of the $N$ friends, in the order in which they lined up, separated by whitespace.

## Output data

The output file `fotbal3.out` will contain the required number.

## Constraints and clarifications

$1 \leq N \leq 100 \, 000$ 

The values of the friends are distinct.

$1 \leq value\ of\ a\ friend \leq 300 \, 000$ 

For tests worth $22$ points 

$1 \leq N \leq 1 \, 000$ 

## Example

`fotbal3.in`
```
6
1 2 3 4 5 6
```

`fotbal3.out`
```
14
```

`fotbal3.in`
```
10
25 4 89 200 100 10 8 31 178 40 36
```

`fotbal3.out`
```
10
```

## Explanation

In the first example, the intervals $[1]$, $[2]$, $[3]$, $[4]$, $[5]$, $[6]$, $[1,2]$, $[1,2,3]$, $[1,2,3,4]$, $[1,2,3,4,5]$, $[1,2,3,4,5,6]$, $[2,3,4]$, $[2,3,4,5,6]$, $[3,4,5,6]$ satisfy the condition.