The Ministry of Numbers has a new chief for a few days. He wanted to make a series of changes in the ministry he leads and started the "reorganization" with the set of natural numbers in 2 stages: first, all the natural numbers were placed without space (or any other separator) between them. After this first stage, the set of natural numbers looked like this:

$1234567891011121314151617181920212223242526272829303132 \\dots$.

The second stage of the "reorganization" consisted of forming new "groups": a group of one digit, a group of $2$ digits, a group of $3$ digits, and so on. Thus, the "reorganized groups" are:

$1$, $23$, $456$, $7891$, $01112$, $131415$, $1617181$, $92021222$, $324252627 \\dots$.

# Task

For a given natural number $N$, display the first and last digit of the N-th group of digits obtained after "reorganization," values separated by a space.

# Input data

The input file `reorganizare.in` contains the value of the natural number $N$.

# Output data

The output file `reorganizare.out` will contain the first and last digit of the N-th group of digits obtained after "reorganization," values separated by a space.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \\ 000 \\ 000$;
* For tests worth $40$ points: $1 \\leq N \\leq 250$;
* For tests worth $60$ points: $1 \\leq N \\leq 40 \\ 000$;

# Example 1

`reorganizare.in`
```
8
```

`reorganizare.out`
```
9 2
```

## Explanation

$9$ and $2$ are the first and last digits of the $8^{th}$ group, which is $92021222$.