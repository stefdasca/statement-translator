## Task

At each international contest he participates in, Marcel collects a few coins from the country he visits. So far, he has collected $N$ coins, with the $i$-th coin having the value $V_i$. Today, because he has a very important but also secret occasion, he decided to use some coins to buy an object with an unknown value. For this reason, he wants to find the maximum value $U$ such that, by taking $K$ coins, he can guarantee that he can pay any non-zero natural value less than or equal to $U$ using only the $K$ chosen coins. He wants to find $U$ for each $K$ from $1$ to $N$.

## Input data

The input file `valoare.in` contains on the first line the natural number $N$. The next line contains $N$ natural numbers $V_i$.

## Output data

The output file `valoare.out` contains $N$ natural numbers, each on a separate line, the $i$-th representing the natural number $U$ considering $K$ equal to $i$.

## Constraints and clarifications

Although Marcel has participated in many international contests, in this problem we will limit $N$ to a maximum of $50\;000$.  
In other words, 
$1 \leq N \leq 50\;000$  
$1 \leq V_i \leq 1\;000\;000\;000$  

For $40\%$ of the points, $N \leq 500$

## Example

`valoare.in`  
`4`  
`1 2 3 4`

`valoare.out`  
`1`  
`3`  
`7`  
`10`

`valoare.in`  
`3`  
`1 2 5`

`valoare.out`  
`1`  
`3`  
`3`

`valoare.in`  
`2`  
`2 2`

`valoare.out`  
`0`  
`0`

## Explanation

In the first example, by taking one coin, we will take the one with value $1$ to guarantee that we can pay for an object of value $1$. For two coins, we will take those with values $1$ and $2$ to guarantee that we can pay for an object with a value between $1$ and $3$. For three coins, we will take those with values $1$, $2$, and $4$ to guarantee that we can pay for an object with a value between $1$ and $7$. For example, we can write $5$ as $1 + 4$, using only the chosen coins. Note: If we had taken the coin with value $3$ instead of the one with value $4$, we wouldn't have been able to pay the sum $7$. By taking all four coins, we guarantee that we can pay for an object with a value between $1$ and $10$. For example, we can write $7$ as $1 + 2 + 4$ or as $3 + 4$.

In the second example, by taking one coin, we will take the one with value $1$ to guarantee that we can pay for an object of value $1$. For two coins, we will take those with values $1$ and $2$ to guarantee that we can pay for an object with a value between $1$ and $3$. By taking all three coins, we guarantee that we can pay for an object with a value between $1$ and $3$, but since we can't pay for an object with a value equal to $4$, we can't guarantee that we can pay for an object with a value between $1$ and a value greater than or equal to $4$.

In the third example, we can't pay for an object with a value equal to $1$, so $U = 0$, no matter how many coins we take.