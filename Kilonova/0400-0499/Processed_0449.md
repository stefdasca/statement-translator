
In Cosmin's garden, there is an apple tree with an unlimited number of apples. His $N$ friends, numbered from $1$ to $N$, will pick apples for $T$ days, according to the following rule:
In the morning of day $T_i$, Cosmin's friends will form a queue at the entrance of the garden, starting with friend $X_i$. Thus, the queue will look like $X_i$, $X_{i+1}$, ..., $X_n$, $X_1$, ..., $X_{i-1}$. On that day, they will pick $Y_i$ apples. Each friend $X_i$ will enter the garden, pick an apple, and return to the queue.
On day $T + 1$, Cosmin randomly selects $K$ friends ($Q_1..Q_k$) and wants to find out how many apples each has collected.

# Task
Write a program to find the number of apples collected by each of the $K$ friends selected by Cosmin.

# Input data
The input file `mere.in` contains:
The first line contains $N \\ T \\ K$, three integers representing the number of friends, the number of days they will pick apples, and the number of questions from Cosmin.
The next $T$ lines each contain two integers, separated by a space, $X_i \\ Y_i$, representing the index of the friend who will enter the garden first and the number of apples that will be picked on day $T_i$.
The last line contains $K$ integers, $Q_i$, representing the indices of Cosmin's friends for whom the number of collected apples is to be found.

# Output data
The output file `mere.out` will contain $K$ integers, on a single line, separated by a space, representing the answers to the $K$ questions.

# Constraints and clarifications
* $1 \\leq X_i \\leq N \\leq 10\ 000\ 000$;
* $1 \\leq T \\leq 200\ 000$;
* $1 \\leq K \\leq 100\ 000$;
* $1 \\leq Y_i \\leq 1\ 000\ 000$.
* For tests worth $30$ points: $1 \\leq X_i \\leq N \\leq 100$, $1 \\leq T \\leq 100$, $1 \\leq K \\leq 100$, $1 \\leq Y_i \\leq 1\ 000$; 
* For tests worth $50$ points: $1 \\leq X_i \\leq N \\leq 200\ 000$, $1 \\leq T \\leq 10\ 000$, $1 \\leq K \\leq 10\ 000$;
* For tests worth $70$ points: $1 \\leq N \\leq 1\ 000\ 000$, $1 \leq T \leq 100\ 000$.

# Example

`mere.in`
```
5 3 4
1 2
3 5
2 7
2 4 1 2
```

`mere.out`
```
4 2 3 4
```

## Explanation

$5$ people will pick apples for $3$ days, as follows:
- On the first day, they will pick $2$ apples, people with indices $1$ and $2$;
- On the second day, they will pick $5$ apples, people with indices $3, 4, 5, 1$ and $2$;
- On the third day, they will pick $7$ apples, people with indices $2, 3, 4, 5, 1, 2, 3$.

Thus, the number of apples collected by each person from $1$ to $N$ is: $1 \\rightarrow 3, 2 \\rightarrow 4, 3 \\rightarrow 3, 4 \\rightarrow 2, 5 \\rightarrow 2$.
