## Stutter

Given a string $S$. We call the stutter of order $k$ of $S$ the string obtained by multiplying each character of $S$ exactly $k$ times. For example, the stutter of order $2$ of the string "andrei" is the string "aannddrreeii", and the stutter of order $3$ of the string "ana" is the string "aaannnaaa". Given a string $A$ and $Q$ strings $B_1, B_2, \dots, B_Q$, for each string $B$, we want to find the maximum order of the stutter of the respective string that appears as a subsequence in the string $A$. For example, for $A = \text{"onomatopee"}$ and $B = \text{"oe"}$, the maximum order of the stutter is $2$, and for $B^\prime = \text{"z"}$, the maximum order of the stutter is $0$.

## Input data

The input file `balbaiala.in` contains on the first line the natural numbers $N$ (the size of the string $A$) and $Q$ (the number of strings $B_i$), the second line contains the string $A$, and the following $Q$ lines contain the strings $B_i$.

## Output data

The output file `balbaiala.out` will contain $Q$ lines, each $i$-th line containing a natural number representing the maximum order of the stutter of the string $B_i$ that appears as a subsequence in the string $A$.

## Constraints and clarifications

The sum of the lengths of the $Q$ queries is less than or equal to $300\ 000$  
For 20 points, $1 \leq N, Q \leq 100$  
For 40 points, $1 \leq N, Q \leq 5\ 000$  
For 70 points, $1 \leq N \leq 30\ 000$ and $1 \leq Q \leq 40\ 000$  
For all points, $1 \leq N, Q \leq 100\ 000$

## Example

balbaiala.in  
`13 3  
abbbaababbaaa  
ab  
ba  
aba`

balbaiala.out  
`3  
4  
3`

## Explanation

$ab$ - The stutter of order $3$, $aaabbb$, appears as a subsequence in $A$, but the stutter of order $4$ does not.  
$ba$ - The stutter of order $4$ appears as a subsequence in $A$, but the stutter of order $5$, $bbbbbaaaaa$, does not.  
$aba$ - The stutter of order $3$, $aaabbbaaa$, appears as a subsequence in $A$, but the stutter of order $4$ does not.