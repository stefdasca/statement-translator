```markdown
Lucky7

We define the function $f$ as follows: $f(x) = $ the sum of the digits of $x$, $modulo 7$. 

## Task 
For a given number $N$, calculate $(f(1) + \dots + f(N)) \mod 1\ 000\ 000\ 007$. 

## Input data

The input file `lucky7.in` contains a single number $N$. 

## Output data

The output file `lucky7.out` will contain the value corresponding to the task. 

## Constraints and clarifications

$1 \leq N < 10^{100\ 000}$ for 10 points 

$1 \leq N < 100\ 000$ for another 10 points 

$N = 10^k , k < 100\ 000$ 

## Examples

`lucky7.in` `lucky7.out`

## Explanations

`1` `1` $f(1) = 1$

`10` `25` $(f(1)+f(2)+f(3)+f(4)+f(5)+f(6)+f(7)+f(8)+f(9)+f(10)) \mod 1\ 000\ 000\ 007 = 25$

`123123213` `369367218$

`1423613231242353464574686796757456346` `319397257$ 

`126791632789139163654532475820489572573247509156021` `304041196$ 
```