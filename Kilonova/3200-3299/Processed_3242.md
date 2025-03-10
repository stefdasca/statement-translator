
# Task

At the freshmen's ball, there are $N$ girls and $M$ boys. Each of them has a beauty coefficient $f_i$, respectively $b_i$. They want to create a maximum number of couples, each consisting of a girl and a boy. The cost of a couple is the difference between the coefficients of the two freshmen. The cost of a maximal matching is the maximum cost of a formed couple. Find the minimum cost of a maximal matching.

# Input data

The first line of the input file `bal.in` contains an integer $N$.
The second line contains $N$ numbers $f_i$.
The third line of the input file contains an integer $M$.
The fourth line contains $M$ numbers $b_i$.

# Output data

The first line of the output file `bal.out` must contain the desired number $K$.

# Constraints and clarifications

* $1 \leq N, M \leq 300\ 000$;
* $1 \leq f_i, b_i \leq 10^9$

|# | Score | Constraints|
| - | - | ------------|
|1|25|$N=M$|
|2|30|$N, M \leq 2000$|
|3|45|No additional constraints|

# Example 1

`bal.in`
```
3
14 10 16
4
17 11 4 17  
```

`bal.out`
```
3
```

## Explanation

Couple 10 with 11 (cost 1), 14 with 17 (cost 3), and 16 with 17 (cost 1). Therefore, the cost of the matching is 3. There are no other matchings with a smaller score.

# Example 2

`bal.in`
```
7
9 17 0 13 14 18 10 
9
19 15 13 11 1 18 5 14 14  
```

`bal.out`
```
3
```
