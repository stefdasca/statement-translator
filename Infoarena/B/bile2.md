# Bile2

Miruna has just learned about probabilities in her math class. She knows that the probability of an event occurring can be expressed as a subunitary ratio, which is equal to the number of favorable cases divided by the total number of cases. For example, if someone needs to say a random digit, the probability that the digit is less than $3$ is $3/10$. The favorable cases are when the person says $0$, $1$, or $2$, and the total number of cases is $10$, representing the total number of digits. After the math class where she learned about probabilities, Miruna came home and started playing with her little brother's balls. She has $N$ balls numbered from $1$ to $N$, which she throws into an urn. Miruna then thinks of $3$ integers $D$, $A$, and $B$. After choosing these numbers, the girl from the story wonders what the minimum number of balls she should draw from the urn, such that the probability of having at least two drawn balls with the absolute difference of their numbers being less than or equal to $D$, is greater than or equal to the ratio $A/B$.

## Input data

The input file `bile2.in` will contain on the first line $2$ integers, $N$ and $D$. The second line will contain the number $A$, and the third line will contain the number $B$. These values have the significance described in the problem statement.

## Output data

The output file `bile2.out` will contain a single integer, representing the minimum number of balls that need to be drawn.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq D < N$

$1 \leq A \leq B \leq 10^{64}$

For $30\%$ of the tests $N \leq 20$, and $A$, $B \leq 10^2$

For an additional $30\%$ of the tests $N \leq 50$, and $A$, $B \leq 10^4$

## Example

`bile2.in`
```
4 1
4
6
```

`bile2.out`
```
3
```

## Explanation

If Miruna had drawn a single ball, the probability would have been equal to $0$. If Miruna had drawn $2$ balls, we would have the following possibilities:
$1\ 2$  
$1\ 3$  
$1\ 4$  
$2\ 3$  
$2\ 4$  
$3\ 4$  

The number of favorable cases is equal to $3$, and the total number of cases is $6$. But $3/6 < 4/6$.

If Miruna draws $3$ balls, we have the cases:
$1\ 2\ 3$  
$1\ 2\ 4$  
$1\ 3\ 4$  
$2\ 3\ 4$  

We observe that the number of favorable cases is equal to the total number of cases.

$4/4 > 4/6$, so $3$ is the correct answer.