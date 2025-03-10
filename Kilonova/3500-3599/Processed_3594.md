Throughout a route, there are multiple tourist attractions identified by a natural number called code. The popularity of a tourist attraction is given by the number of prime divisors in the prime factorization of its code. The more prime divisors a code has, the more popular the attraction with that code is. We call a popular sequence a succession of tourist attractions that contains only one attraction with maximum popularity, and it is either at the beginning or at the end of the sequence. The length of a popular sequence is given by its number of attractions.

# Task

Knowing the number $N$ of tourist attractions on the route and their $N$ codes ($c_1,c_2,\dots,c_N$), determine:
1. The tourist attractions with maximum popularity,
2. The maximum length of a popular sequence of the form ($c_i,c_{i+1},\dots,c_j$), $1 \leq i \leq j \leq N$

# Input data

The file `traseu.in` contains on the first line the number $N$ of attractions and the task $C$ (separated by a space), and on the second line $N$ natural numbers separated by spaces, representing the codes of the tourist attractions.

# Output data

The file `traseu.out` will contain:
- for task 1: a sequence of numbers separated by spaces representing the codes of the most popular tourist attractions, in the order they appear in the input file;
- for task 2: a single value representing the maximum length of a sequence of successive numbers from the given array, which contains only one attraction of maximum popularity located at one of its ends.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$;
* The numbers on the second line of the input file are non-zero and less than or equal to $10^6$;
* For task $1$, $45$ points are awarded;
* For task $2$, $45$ points are awarded;
* A total of $10$ points are awarded by default.

# Example 1

`traseu.in`
```
8 1 
12 6 30 18 10 50 15 70
```

`traseu.out`
```
30 70
```

## Explanation

The task is $1$. Among the $8$ tourist attractions, the most popular are those with codes $30$ and $70$, each having $3$ prime divisors.

# Example 2

`traseu.in`
```
8 2 
12 6 30 18 10 50 15 70
```

`traseu.out`
```
5
```

## Explanation

The maximum length popular sequences can be `30 18 10 50 15` or `18 10 50 15 70`.