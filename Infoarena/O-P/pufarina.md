# Pufarina

In the faraway land of Northern Pufarina, the time has come for the pufarine elections. Pufarina has a total population of $50000$ inhabitants. Among them, $N$ people are running for the position of pufarin. This time, Georgică's role is not to eat puffs, but to take care of counting the votes. For each candidate $i$, the percentage of the total votes obtained by them, $p[i]$, is known. Since counting votes is too simple a task for Georgică, he asks himself the following question: What is the minimum possible number of people who participated in the vote? If this minimum number is greater than $50000$, it is evident that the pufarine elections have been rigged. Your mission is to answer Georgică's question.

## Input data

The input file `pufarina.in` contains the first line with $T$, the number of tests. Next, for each test, the first line will contain the natural number $N$, and the following line will contain $N$ real numbers $p[i]$, the percentages of those $N$ candidates.

## Output data

The output file `pufarina.out` will contain $T$ lines, and each line $i$ will contain the answer to Georgică's question $i$. If the elections in test $i$ are correct, the minimum possible number of people who participated in the vote will be printed, and if not, `ALEGERI FRAUDATE` will be printed.

## Constraints and clarifications

$T = 1000$  
$1 \leq N \leq 10$  
$0 < p[i] \leq 100$  

It is guaranteed that Georgică has counted the votes correctly and that the sum of the percentages of the $N$ candidates is equal to $100$. The percentages have exactly $3$ decimal places.

## Example

`pufarina.in`  
`2`  
`2`  
`50.000 50.000`  
`2`  
`99.999 0.001`  

`pufarina.out`  
`2`  
`ALEGERI FRAUDATE`  

## Explanation

In the first test, there are $2$ candidates. Both have equal percentages, $50\%$, so the minimum number of people who voted is equal to $2$. In the second test, the minimum number of voters is equal to $100000$.