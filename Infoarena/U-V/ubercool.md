## Task

We all know that the Freshmen Ball of the Faculty of Mathematics and Informatics at the University of Bucharest is in two days and it's the last chance for a student named $IWD$ to take $IWM$ out in the city. Since $IWM$ is a mathematics student, and $IWD$ wants to impress her, he thought of the following problem: Given a number $X$, can he say if it is ubercool? A number is ubercool if it is of the form $a^b$, where $a$ is a prime number and $b \geq 2$. Since $IWD$ is very nervous, he asks you to give him the solution.
 
## Input data

The input file `ubercool.in` contains in the first line the number $T$, the number of test cases, and then on line $i+1$, $1 \leq i \leq T$, contains a number $X$.

## Output data

The output file `ubercool.out` contains $T$ lines. On line $i$, $1 \leq i \leq T$, print "DA" if the number $X$ on line $i+1$ of the input is ubercool, "NU" otherwise.

## Constraints and clarifications

$1 \leq T \leq 5000$

$0 \leq X \leq 10^{18}$

The quotes in the output are for clarity. They should not be displayed.

$IWD$ suggests you use the 64-bit data type, specifically `long long`.

## Example

`ubercool.in` 

```
4
2
4
6
27
```

`ubercool.out`

```
NU
DA
NU
DA
```

## Explanation

$2 = 2^1$, so it is not ubercool,

$4 = 2^2$, so it is ubercool,

$6 = 2 \cdot 3$, so it is not ubercool,

$27 = 3^3$, so it is ubercool.