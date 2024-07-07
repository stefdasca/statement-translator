
Spider is a spider who lives in the house of a programmer. From the programmer, Spider has inherited the passion for numbers and programs. Given these circumstances, Spider has decided not to weave his web in the traditional way but to use the information learned from the programmer, adopting a methodical approach. Therefore,

Spider proceeds as follows:
- chooses $n$ points arranged in a circle and numbers them from $1$ to $n$ (clockwise);
- calculates the distances between any two points obtaining only distinct natural numbers;
- chooses a starting point $k$.
- establishes the following rule to follow when weaving the web: each day he will weave one thread; if the day's number is odd, then he weaves the thread from the point he is at to the next point (also clockwise, and after the point numbered $n$ follows the point numbered $1$), and if the day's number is even Spider weaves a thread between the point he is at and the point he reaches by skipping one point;
- stops when he has to weave a thread between two points that already have a woven thread between them.

# Task
Write a program to solve the following requirements:
1. Determine the number of days needed to weave the web and the point where he stopped.
2. Find the lengths of the woven threads together with their endpoints, in descending order of thread lengths. The endpoints of the threads will be displayed in ascending order.

# Input data

The first two lines of the input file `spider.in` contain two integers, $n$ and $k$, representing the number of chosen points and the starting point. On the next $n$ lines are $n$ distances $d_{ij}$, separated by space, representing the distance between points $i$ and $j$.

# Output data

The first line of the output file `spider.out` will contain two integers $x$ and $p$, the number of days and the point where Spider stopped. On the next $p$ lines will be three values, representing the lengths of the threads and their endpoints, in descending order of thread lengths. The endpoints of the threads will be displayed in ascending order.

# Constraints and clarifications

* $1 \leq n \leq 100$; 
* $1 \leq k \leq n$;
* $0 \leq d_{ij} \leq 50\ 000$.

# Example

`spider.in`
```
4
2
0 5 8 7
5 0 3 10
8 3 0 4
7 10 4 0
```

`spider.out`
```
5 1
10 2 4
8 1 3
7 1 4
5 1 2
3 2 3
```

## Explanation

~[spider.png|width=20em]

On day $1$, Spider starts from point $2$ and weaves a thread to point $3$. On day $2$, from point $3$ he weaves a thread to point $1$ (skipping point $4$). On day $3$ from point $1$ he weaves a thread to point $2$. On day $4$ from point $2$ he weaves a thread to point $4$ (skipping point $3$). On day $5$ from point $4$ he weaves a thread to point $1$ and stops.
