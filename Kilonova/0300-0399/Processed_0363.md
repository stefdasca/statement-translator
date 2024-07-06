# Task

Mr. X enjoys solving and especially talking a lot about bitwise operations, even at the New Year's Day party. While drinking with his friends, he came up with the following challenge.

There are $q$ queries, and in each query you are given a positive integer $a_i$ ($i=0\ldots q-1$). You are required to answer the following question:

What is the bitwise XOR of the integers in the interval [$0, a_i$] and what is the maximum bitwise XOR we can get by removing **exactly** one integer from that interval?

Your task is to solve the challenge of Mr. X.

# Input data

The first line of the input contains $q$, the number of queries ($1 \le q \le 2 * 10^5$).

Each of the next $q$ lines contains a positive integer $a_i$, describing a query ($1 \le a_i \le 10^9$).

For tests worth $15$ points: $1 \le q, a_i \le 1000$  
For tests worth $15$ points: $1 \le a_i \le 10^4$  
For tests worth $20$ points: $1 \le a_i \le 10^6$ and  $1 \le q \le 50$  

# Output data

Print $q$ lines, the answers to each query. Every line should contain two numbers, namely, the bitwise XOR of the integers in the interval [$0, a_i$], and the maximum bitwise XOR we can get by removing one integer from the interval.

`stdin`
```
5
29
14
9
12
31
```

`stdout`
```
1 29
15 15
1 9
12 15
0 31
```