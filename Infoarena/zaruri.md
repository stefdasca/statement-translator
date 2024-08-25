# Dice

After a year of dedicated efforts to join the National Craps Team, Vasile returns to school, needing to finalize his grades. The physics teacher, a doctor in randomized grading methods, proposes the following game: Vasile will roll a die at most $N$ times. After any round, he can stop, and the score obtained from the last roll (the value on the top face of the die) will be his final grade in physics. Vasile would like to know what average score he could achieve in this test, assuming he has an optimal strategy to maximize the result.

## Input data

The input file `zaruri.in` will contain on its only line the number $N$.

## Output data

The output file `zaruri.out` will contain a real number, the maximum average score that Vasile can obtain.

## Constraints and clarifications

$1 \leq N \leq 20$  
The answer will be considered correct if the absolute difference between it and the correct answer is at most $10^{-7}$  
Vasile performed very well on the team this year, but he will not repeat this performance next year, as he does not want to accidentally end up at the Olympians' Exam.

## Example

`zaruri.in`  
$1$

`zaruri.out`  
$3.5$  

`zaruri.in`  
$2$

`zaruri.out`  
$4.25$

## Explanation

In the first example, Vasile rolls the die once. Each value from $1$ to $6$ can be obtained with a probability of $1/6$. Thus, on average, he will obtain $(1 + 2 + 3 + 4 + 5 + 6)/6$ points. Although the calculations become more complicated, even in the second example, Vasile will not manage, on average, to obtain a passing grade.