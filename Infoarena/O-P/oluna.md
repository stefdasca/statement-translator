# One Month

## Task

Today marks exactly $1$ month since the beginning of Antonio and Antonia's relationship. Because Antonio forgot to buy tulips for Antonia, which are her favorite flowers, she decided to punish him. Therefore, Antonia will ask Antonio $Q$ questions: I have a number $N$. In how many ways can this number be written as the sum of $3$ even non-zero natural numbers? Two writing methods of a number are considered distinct if at least one number in the two methods is different. 

## Input data

The input file `oluna.in` contains on the first line a natural number $Q$, representing the number of questions from Antonia. Each of the next $Q$ lines will contain a natural number $N$, with the meaning given in the statement. 

## Output data

The output file `oluna.out` will contain $Q$ lines. On each line $i$, there will be a single natural number, representing the answer to Antonia's $i^{th}$ question. 

## Constraints and clarifications

$1 \leq Q \leq 1\ 000$

$1 \leq N \leq 10^9$

## Example

`oluna.in` 
```
2 
111 
10 
```

`oluna.out` 
```
0 
2 
```

## Explanation

Number $111$ cannot be obtained according to the task. Number $10$ can be written as: $2 + 2 + 6$ or $2 + 4 + 4$.

`oluna.in` 
```
2 
2 
20 
```

`oluna.out` 
```
0 
8 
```

$2$ cannot be written as the sum of $3$ even non-zero natural numbers. The $8$ possibilities are: $2 + 2 + 16$, $2 + 4 + 14$, $2 + 6 + 12$, $2 + 8 + 10$, $4 + 4 + 12$, $4 + 6 + 10$, $4 + 8 + 8$, $6 + 6 + 8$.