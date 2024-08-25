##  Gigel and the Remainders

Bored during art class, our mathematician Gigel noticed a very large piece of paper on the floor. Turning the paper over, he saw a very long sequence of digits and uppercase English letters. After much thought, Gigel realized that this piece of paper actually had a very large number written in a base $B$, where $B \leq 16$. Being very ingenious, he asked himself the following question: What is the remainder of the number written on the paper, in base $10$, when divided by a number $K$, in base $10$? Because Gigel is a math whiz and already knows the answer to this question, he invites you, the curious, to answer the question as well.

##  Input data

The input file `gsr.in` contains on the first line two natural numbers, $B$ and $K$, with the significance from the statement. The second line contains the characters from the sheet of paper. 

##  Output data

In the output file `gsr.out` there will be a single natural number, the remainder of the division of the number on the paper by the number $K$.

##  Constraints

$1 \leq B \leq 16$

$1 \leq K \leq 1\,000\,000\,000$

The sheet of paper contains at most $1\,000\,000$ characters

##  Example

`gsr.in`
```
2 3
1110
```

`gsr.out`
```
2
```

##  Explanation

$1110$ in base $10$ is $14$, and the remainder of $14$ divided by $3$ is $2$.