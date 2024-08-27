# Guards

The head of a company on an unknown planet wants the company's headquarters to be guarded at every whole moment of time from $1$ to $T$. He has received $N$ offers from security firms in the form $a \; b \; c$, meaning that for the price of $c$ units, a guard can be hired to protect the company for one unit of time, but only at a moment of time $t$ within the closed interval $[a,b]$ $(a \leq t \leq b)$. On the planet where the company is located, technology is not very advanced, and therefore, your help is needed to find out the minimum cost the head of the company should pay so that the company is guarded at every whole moment of time from $1$ to $T$. Of course, several guards from the same security firm can be hired, and each hired guard guards the company for exactly one unit of time.

## Input data

The input file `gardieni.in` contains on the first line two natural numbers $N$ and $T$ having the meaning from the problem statement. Followed by $N$ lines, each containing three natural numbers $a \; b \; c$ representing the offers of each security firm. 

## Output data

The output file `gardieni.out` contains on the first line the natural number $MIN$, representing the minimum cost that must be paid so that the company is guarded at every whole moment of time from $1$ to $T$. 

## Constraints and clarifications

$1 \leq N \leq 50 \; 005$

$1 \leq T \leq 1 \; 000 \; 000$

$1 \leq a \leq b \leq T$

$1 \leq c \leq 220$

However, if we choose any $11$ offers from the security firms and consider their associated intervals $[a_1,b_1]$, $[a_2,b_2]$, $\dots$, $[a_{11},b_{11}]$, there does not exist a natural number $x$ such that $a_1 \leq x \leq b_1$, $a_2 \leq x \leq b_2$, $\dots$, $a_{11} \leq x \leq b_{11}$. It is guaranteed that at every moment of time there is at least one guard who can be hired.

## Example

`gardieni.in`
```
3 5
2 4 3
1 3 1
5 5 2
```

`gardieni.out`
```
8
```

## Explanation

For the times $1$, $2$, and $3$, a guard from the second firm will be hired, and a total of $1+1+1=3$ will be paid. For time $4$, a guard from the first firm will be chosen at the cost of $3$ units, and at time $5$, a guard from the third firm will be chosen at the cost of $2$ units. The total cost will be $1+1+1+3+2=8$.