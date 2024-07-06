Our sports teacher is a good friend of the math teacher. For this reason, during the sports class, he invents all sorts of problems and then asks the math teacher to solve them. Today, during the sports class, $N$ students are participating, each wearing a t-shirt with numbers $1, 2, \dots, N$. At the beginning of the class, the $N$ students line up in the order $p_1, p_2, \dots, p_N$ (i.e., the student with t-shirt $p_1$ stands at position $1$ in the line, the student with t-shirt $p_2$ stands at position $2$, etc., the positions in the row being numbered from $1$ to $N$ from left to right). The sports teacher then says: "On my command, switch places as follows: in position $i$, the student who is currently at position $p_{p_i}$ should stand (for each $1 \leq i \leq N$)."

For example, if $N=6$ and initially, the students arranged themselves as follows: $3, 1, 4, 2, 6, 5$
* After the first command: $4, 3, 2, 1, 5, 6$

Notice that at position $1$ is student $3$ and at position $3$ is student $4$. After the first command, at position $1$ will be student $p_{p_1}=p_3=4$. At position $2$ is student $1$, and at position $1$ is student $3$. After the first command, at position $2$ will be student $p_{p_2}=p_1=3 \dots$
* After the second command: $2, 4, 1, 3, 6, 5$.

Notice that in the configuration obtained after the first command at position $1$ was student $4$ so after one more command, at position $1$ will be student $p_4$, i.e., student $2$. At position $2$ was student $3$, so after one more command, at position 2 will be student $p_3$, i.e., student $4$ etc.
* After the third command, the configuration $1, 2, 3, 4, 5, 6$ is obtained.
* And after the fourth command, the initial configuration is restored.

The sports teacher asks the math teacher: what is the minimum number of commands that need to be given so that the students return to the initial configuration? And what would be the smallest initial configuration (considering the lexicographical order) for which it takes the same minimum number of commands to return to the initial configuration.

# Task

Write a program to help the math teacher answer the two questions posed by the sports teacher.

# Input data

The input file `sport.in` contains on the first line a natural number $N$ representing the number of students. The second line contains $N$ distinct values between $1$ and $N$, representing the initial configuration of the students.

# Output data

The output file `sport.out` will contain two lines. The first line will contain a natural number representing the minimum number of commands that need to be given so that the students return to the initial configuration. The second line will contain $N$ distinct values between $1$ and $N$, representing the smallest initial configuration (considering the lexicographical order) for which the same minimum number of commands is required to return to the initial configuration.

# Constraints and clarifications

* $1 \leq N \leq 500$
* The values written on the same line in the input file, respectively in the output file, are separated by spaces.
* We say that a configuration $p=(p_1, p_2, \dots, p_N)$ is lexicographically smaller than another configuration $q=(q_1, q_2, \dots, q_N)$ if there exists an index $k, 1 \leq k \leq N$ such that $p_i=q_i$, for any $1 \leq i < k$ and $p_k < q_k$.
* The minimum number of commands that need to be given is $\leq 2 \ 000 \ 000 \ 000$ (two billion).
* $50$% of the points are given for the first task. The full score is given for solving both tasks.

# Example

`sport.in`
```
6
3 1 4 2 6 5
```

`sport.out`
```
4
1 2 4 5 6 3
```