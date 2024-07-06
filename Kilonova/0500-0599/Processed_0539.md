Sure! Here's the translated competitive programming problem statement in English:

---

Dan is a very busy caveman: he has to break $n$ boulders. For each boulder $i$, the number of days $z_i$ necessary to break it and the deadline $d_i$, meaning the last day by which it should be broken, are known.

Dan knows that the most efficient way to work is to focus on a single boulder each day. If he starts working on a particular boulder, he will work on it continuously until he breaks it, without interspersing days working on other boulders or taking breaks. Also, Dan will not take rest days between finishing one boulder and starting work on the next one.

A boulder $i$ is considered broken *before the deadline* if the number of the last day Dan works on the boulder $i$ is **less than or equal** to $d_i$.

# Task

Given the number $n$ of boulders, as well as the number of days required to break each boulder and the deadline by which it should be broken, determine a schedule for working on the $n$ boulders such that a maximum number of boulders are broken *before the deadline*.

# Input data

The first line of the input file `bolovani.in` will contain the number $n$ of boulders. The next $n$ lines will contain two integers each, with the $i$-th of these lines containing the numbers $z_i$ and $d_i$ separated by a space, indicating the number of days required to break the boulder $i$, and the last day by which boulder $i$ should be broken, respectively.

# Output data

The first line of the output file `bolovani.out` will contain the number of boulders broken *before the deadline*. The next $n$ lines will contain two numbers separated by a space, indicating the day Dan starts working on the boulder $i$ and the day Dan finishes breaking the boulder $i`. If there are multiple solutions, any can be displayed.

# Constraints and clarifications

* $1 \le n \le 10\ 000$
* $1 \le z_i, d_i \le 1\ 000\ 000\ 000$
* Dan starts breaking the boulders on day $1$.
* Dan must break all $n$ boulders, even if some will not be broken *before the deadline*.

|# | Points | Constraints|
| - | - | ------------|
|1|20|$n \le 10$|
|2|20|$d_1 = d_2 = ... = d_n$|
|3|60|No additional constraints|

# Examples

`bolovani.in`
```
5
4 6
3 7
2 8
5 9
6 11
```

`bolovani.out`
```
3
12 15
1 3
4 5
16 20
6 11
```

# Explanation

Dan has to break $n=5$ boulders. He can break $3$ of them *before the deadline* if he works:

* on boulder $1$ from day $12$ to day $15$, inclusive, finishing breaking it after the deadline on day $6$.
* on boulder $2$ from day $1$ to day $3$, inclusive, finishing breaking it before the deadline on day $7$.
* on boulder $3$ from day $4$ to day $5$, inclusive, finishing breaking it before the deadline on day $8$.
* on boulder $4$ from day $16$ to day $20$, inclusive, finishing breaking it after the deadline on day $9$.
* on boulder $5$ from day $6$ to day $11$, inclusive, finishing breaking it before the deadline on day $11$.

---

Please, let me know if there are any other specific requirements or sections you'd like me to adjust!