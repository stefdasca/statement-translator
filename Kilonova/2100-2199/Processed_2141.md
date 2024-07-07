# Andino has found a new passion — music. As they say, hard work always pays off, so here he is at his first concert! Andino, being an artist who became popular very quickly, gathered a large audience at his concert, arranged in the form of a matrix with $N$ rows and $M$ columns.

Each fan of Andino can have one of two states: *in the vibe*, encoded in the matrix structure with $1$ and *bored*, encoded in the matrix structure with $0$. Andino observed this among the crowd and wants to change people's states, so he makes the following decision: during his concert, Andino will *change the vibe* of his fans located within a submatrix defined by the top-left corner coordinates $(x_1, y_1)$ and the bottom-right corner coordinates $(x_2, y_2)$.

By *changing the vibe* we mean that the state of any fan changes (the state becomes *in the vibe* from *bored* and vice versa). Throughout the concert, Andino *changes the vibe* of his fans exactly $T$ times.

# Task

At the end of the concert, Andino wants to know how the audience felt during the concert and asks $Q$ of his fans what their state is. A question has the following form: "What is the state of the fan at coordinates $(x_Q, y_Q)$?". Being busy, Andino asks you to help him get the answers to these questions.

# Input data

The first line contains two integers, $N$ and $M$, representing the number of rows and, respectively, the number of columns of the matrix representing the states of Andino's fans.

The next $N$ lines contain $M$ numbers from the set $\{0, 1\}$, representing the states of Andino's fans as described in the statement above.

The $(N+2)$-nd line contains the number $T$, representing the number of *vibe changes* Andino makes during the concert. The next $T$ lines contain 4 numbers $x_1$, $y_1$, $x_2$, $y_2$ representing the submatrix chosen for the *vibe change* defined by the top-left corner coordinates $(x_1, y_1)$ and the bottom-right corner coordinates $(x_2, y_2)$.

The next line contains the number $Q$ representing the number of questions Andino has, and the next $Q$ lines contain 2 numbers $x_Q$ and $y_Q$ corresponding to the question in the form "What is the state of the fan at coordinates $(x_Q, y_Q)$?".

# Output data

The output file must contain $Q$ lines which contain the answer to Andino's questions defined above.

# Constraints and clarifications

* $1 \leq N,M \leq 2\ 000$
* $1 \leq T \leq 100\ 000$
* $1 \leq Q \leq 100\ 000$
* For each *vibe change*, $1 \leq x_1, y_1, x_2, y_2 \leq 2\ 000$, $x_1 \leq x_2$ and $y_1 \leq y_2$.
* For each of Andino's questions, $1 \leq x_Q \leq N$ and $1 \leq y_Q \leq M$.
* Andino will only ask questions after the concert is over.
* For tests worth $20$ points, $1 \leq N,M \leq 100$.
* For tests worth $50$ points, $1 \leq N,M \leq 800$.
* For tests worth $100$ points, $1 \leq N,M \leq 2\ 000$.

# Example 1

`concert.in`
```
2 4
0 1 1 0
1 0 1 0
2
1 1 2 3
1 2 1 4
3
1 1
1 3
2 4
```

`concert.out`
```
1
1
0
```

## Explanation

After the first *vibe change*, the state of the fans is defined as follows:
```
1 0 0 0
0 1 0 0
```

After the second *vibe change*, the state of the fans is defined as follows:
```
1 1 1 1
0 1 0 0
```

The state above is the state of the fans at the end of the concert, from which we have the answer in the example.

# Example 2

`concert.in`
```
5 5
0 0 0 1 0
1 0 0 1 1
1 1 0 1 1
0 1 0 1 1
1 1 0 1 0
3
2 2 4 4
1 3 2 4
4 3 5 5
5
1 1
3 3
4 3
1 3
2 4
```

`concert.out`
```
0
1
0
1
1
