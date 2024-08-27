# Parrots

## Task

K0kalaru47 asks you to tell him the maximum number of parrot schemes that can be carried out in the initial situation and in each of his plans, modulo $10^9 + 7$.

## Input data

The first line of the input file `papagali.in` contains $N$ and $K$.  
The second line contains $A_1$, $A_2$, $\dots$, $A_K$.  
The third line contains $Q$.  
The fourth line contains the values $X_1$, $X_2$, $\dots$, $X_Q$.  

## Output data

The first line of the output file `papagali.out` will contain the number of parrot schemes that can be realized in the initial situation.  
On the $i+1$ line $(1 \leq i \leq Q)$ will contain the maximum number of parrot schemes that can be obtained by acquiring $X_i$ new parrots. These numbers will be printed modulo $10^9 + 7$.  

## Constraints and clarifications

$0 \leq N, Q \leq 200,000$  
$1 \leq K \leq 200,000$  
$0 \leq X_i \leq 400,000$  
$N$, $A_i$, and $X_i$ are even

For tests worth 10 points, $K = 1$  
For tests worth 30 points, $Q = 0$  
For tests worth 20 points, $K, Q \leq 2000$ and $X_i \leq 4000$  

## Example

`papagali.in`  
```
6 2  
4 2  
1  
2  
3  
2  
```

`papagali.out`  
```
45  
630  
4  
3  
2  

```

## Explanation

In the first example, there are $45$ schemes that can be performed with the initial parrots. Some of these schemes are:  
We place the parrots of the first species in the first $4$ positions and the parrots of the second species in the last $2$ positions. We form pairs between the parrots on positions $1$ and $2$, $3$ and $4$, $5$ and $6$.  
We place the parrots of the first species in the first $4$ positions and the parrots of the second species in the last $2$ positions. We form pairs between the parrots on positions $1$ and $3$, $2$ and $4$, $5$ and $6$.  
We place the parrots of the first species on positions $1$, $3$, $5$ and $6$ and the parrots of the second species on positions $2$ and $4$. We form pairs between the parrots on positions $1$ and $6$, $3$ and $5$, $2$ and $4$.  
We place the parrots of the first species on positions $1$, $2$, $4$ and $6$ and the parrots of the second species on positions $3$ and $5$. We form pairs between the parrots on positions $1$ and $6$, $3$ and $5$, $2$ and $4$.  

If in the plan from the first example we acquire two more parrots of the second species, we will be able to make $630$ schemes, this being the maximum possible number.