# Task

After solving many problems, you have arrived at Fibofest and are ready to relax. Unfortunately, to gain access to all the festival's entertainments, you must first help the organizers with a list of $Q$ questions. Initially, the organizers will give you a number $K$ and two lists, each containing $K$ natural numbers, named $A$ and $W$. With these, an infinite sequence of numbers $F$ will be defined according to the following rules:

* $F_i = A_i$, for $1 \leq i \leq K$;
* $F_i = \sum_{j=1}^K W_j \times F_{i - j}$, for $i > K$;

Using the information above, your objective is to answer the $Q$ questions, which have the following form:
$N$ - What is the value of $F_N$ modulo $1 \ 000 \ 000 \ 007$?

# Input Data

The first line contains the number $K$.  
The second line contains $K$ values, representing the array $A$.  
The third line contains $K$ values, representing the array $W$.  
The fourth line contains the number $Q$.  
The following $Q$ lines will each contain one number, $N$, representing the current question.

# Output Data

The answers to the $Q$ questions should be printed one per line, for a total of $Q$ lines in stdout.

# Constraints and Clarifications

* $1 \leq K, Q \leq 200$;
* $0 \leq A_i, W_i \leq 1 \ 000 \ 000 \ 000$;
* $1 \leq N_i \leq 1 \ 000 \ 000 \ 000$;

# Example

`stdin`
```
2
0 1
1 1
5
6
4
5
3
7
```

`stdout`
```
5
2
3
1
8
```

## Explanation

The sequence $F$ is the Fibonacci sequence: $0$, $1$, $1$, $2$, $3$, $5$, $8$, $13$, $\ldots$.