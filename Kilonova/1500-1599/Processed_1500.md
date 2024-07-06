Zeno has $n$ boxes of candies, and in each box, there is a non-zero natural number of candies. Zeno can distribute candies from all the boxes to his colleagues in two ways: equal or differentiated. An equal distribution is done as follows:

* The number of colleagues who receive candies from each box is the same (if $k$ colleagues receive candies from the first box, then $k$ colleagues will receive candies from the second box, and from the third box, and so on);
* The candies from each box are shared equally among the $k$ colleagues, each receiving a non-zero amount of candies;
* In the end, each box must have the same number of candies left (possibly zero) which will be for Zeno. For example, if $n = 3$, and the boxes contain $14, 23$, and respectively $17$ candies, from the first box he gives $4$ candies to $3$ colleagues, from the second box he gives $7$ candies to $3$ colleagues, and from the last box he gives $5$ candies to $3$ colleagues, leaving $2$ candies in each box.

A differentiated distribution is done as follows:

* Among the colleagues who receive candies from the same box, each colleague receives a different number of candies (non-zero), with no two colleagues receiving the same number of candies from the same box;
* Zeno offers candies to the largest possible number of colleagues from each box;
* The differences between the number of candies received consecutively by two colleagues are distinct two by two. For example, if $n = 3$, and the boxes contain $14, 23$, and $17$ candies respectively, the candies from the *first box* can be distributed as $(3, 4, 6, 1)$, the candies from the *second box* as $(6, 2, 7, 1, 3, 4)$, and the candies from the *third box* can be distributed as $(2, 1, 3, 7, 4)$.

# Task

Given $n$, the number of boxes, and the number of candies in each box, write a program that determines:

$a)$ The maximum number of colleagues who can receive candies if Zeno chooses the equal distribution.

$b)$ A method of distributing the candies from each box if Zeno chooses the differentiated distribution.

# Input data

The input file `bomboane.in` contains on the first line two natural numbers $p$ (the number of the requirement to be solved) and $n$ (the number of boxes), separated by a space. On the next line, there are $n$ natural values, separated by a space, representing the number of candies in each box.

# Output data

If $p = 1$ only requirement $a)$ from the task will be solved. In this case, the output file `bomboane.out` will contain a natural value representing the maximum number of colleagues who can receive candies if Zeno chooses the equal distribution.

If $p = 2$, only requirement $b)$ will be solved. The output file `bomboane.out` will contain $n$ lines. On each line $i$, the first value $nri$ represents the maximum number of colleagues who can receive candies from box $i$, followed by $nri$ values separated by a space representing a method of distributing the candies from box $i$ if Zeno chooses the differentiated distribution.

# Constraints and clarifications

* _$1 \leq p \leq 2$_
* If $p = 1$ then $1 \leq n \leq 10 \ 000$ and $1 \leq$ number of candies in boxes $\leq 10^6$
* If $p = 2$ then $1 \leq n \leq 200$ and $1 \leq$ number of candies in boxes $\leq 10^5$
* If there are multiple solutions, any can be displayed.
* For solving each task requirement, $50$% of the score is awarded.

# Example 1

`bomboane.in`

```
1 3
14 23 17
```

`bomboane.out`

```
3
```

# Explanation

Only point $a)$ is solved. The maximum number of colleagues who can receive candies if Zeno chooses the equal distribution is $3$.

# Example 2

`bomboane.in`

```
2 3
14 23 17
```

`bomboane.out`

```
4 3 4 6 1
6 6 2 7 1 3 4
5 2 1 3 7 4
```

# Explanation

Only point $b)$ is solved. From the first box, a maximum of $4$ colleagues can receive candies. A method of distribution such that each colleague receives a different number of candies and the differences between the candies received by two consecutive colleagues are distinct two by two is $(3, 4, 6, 1)$. The solution $(1, 2, 7, 4)$ is also correct.