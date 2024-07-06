After conquering all the 16 races, Sora and Shiro have finally managed to challenge the god Tet to a duel. Tet randomly generated an undirected graph with edge costs. In the end, he asked the two characters Q questions in the form: what is the shortest path from node x to node y? Because he knows it is a hard problem, he is content with paths that are as short as possible, not necessarily the shortest ones.

# Task

Tet randomly generated an undirected graph with edge costs and then asked Q questions about the shortest paths between pairs of nodes.

# Input data

The first line of the input file `nolife.in` will contain a natural number N (number of nodes) and a natural number M (number of edges). The next M lines will contain three numbers x, y, and z, representing an edge with length z between nodes x and y. The following line will contain a natural number Q. The next Q lines will each contain two numbers, x and y – the nodes between which we need to find the shortest possible path.

# Output data

In the output file `nolife.out`, the answer for each question will be displayed, one per line. An answer must describe a path between nodes x and y as follows: the first number on the line is the number of nodes through which the path passes, followed by the nodes in the order from x to y. If you choose not to answer a question, display just 0 for that question.

# Constraints and clarifications

* $1 \ \leq N \ \leq 100 \ 000$;
* $1 \ \leq M \ \leq 300 \ 000$;
* $1 \ \leq Q \ \leq 20 \ 000$;
* Because Tet is a programmer demigod, he indexes node indices from 0 to $N-1$;
* It is guaranteed that there is a path between all the nodes in the questions;
* The best contestant will win Jibril.

# Scoring

Tet knows that life is a competition, so he will score you as follows: For each test, you will receive a raw score, which represents the sum of the scores for each question. For each question, you get 1 point if you find an optimal path length, otherwise, you will receive a number of points calculated using the formula: 

$$\large \displaystyle \frac{0.9}{2^{\left(\frac{\text{found\_length}}{\text{optimal\_length}}-1\right)\times 4}}$$

We know it sounds complicated, but it just means you get a maximum of 0.9 points for any non-optimal score, and for every 25% deviation from the optimal, your score will be halved. During the test, you will receive this raw score, but for the final score, we will normalize the raw scores of all contestants and the official source. That means you will get for each test your raw score divided by the best score on that test among all sources (including the official one).

# Example

`nolife.in`
```
5 6
1 2 1
1 4 2
4 3 4
2 3 2
4 0 3
3 0 6
4
1 2
2 0
1 4
3 4
```

`nolife.out`
```
2 1 2 
4 2 1 4 0 
2 1 4 
2 3 4
```

## Explanation

This solution receives a full score on the test, as all paths are optimal.