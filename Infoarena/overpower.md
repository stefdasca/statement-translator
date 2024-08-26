## Overpower

The dispute between Unaiv High School and the Theoretical Computer Science Institution is escalating. Arguments arise such as: "Our teachers are more lenient with students," "We don't even know our teachers," or "During 'alternative school,' you should try holding some classes too." Tahref, a remarkable teacher, exhausted by the endless conflict between the school and the institution, decides to put an end to the discord by breaking into Unaiv's security system and taking over (and Unaiv changes their directors every 2 years anyway). In order to infiltrate the school's systems, Tahref needs to solve the following problem: The power of a number is the highest value such that it can be written as a product of two natural numbers, with one of the two being different from 1 and having the exponent. Specifically, the power of the interval is given. Several intervals are provided, and for each interval, the power is requested.

## Input data

The first line contains $Q$, the number of queries. The next $Q$ lines contain two numbers $A$ and $B$, the limits of the interval.

## Output data

The output file contains $Q$ lines, each line containing the answer for the $i$-th query.

## Constraints

To pass a test, the answer to all questions in that test must be correct. Tests are grouped. To get the score for a subtask, the solution must pass all the tests in that subtask.
$1 \leq Q \leq 50$
$2 \leq A \leq B \leq 10^{18}$ 

Subtasks
- 10 points: $2 \leq A \leq B \leq 100$ (test 1)
- 10 points: $2 \leq A \leq B \leq 10^6$ (test 2)
- 20 points: $2 \leq A \leq B \leq 10^{12}$ (tests 3-4)
- 10 points: $A = B$, $2 \leq A \leq 10^{18}$ (test 5)
- 50 points:

## Initial Constraints

(tests 6-10)

## Example

`overpower.in`
```
4
2 2
50 51
25 30
34 37
```
`overpower.out`
```
1
2
3
2
```

## Explanation for the first example

There are 4 queries:
The first interval contains the number $2$, which can be written as $1 \times 2^1$, with the maximum exponent being $1$.
The second interval contains the number $50 = 2 \times 5^2$, with the maximum exponent being $2$.
The third interval contains the number $27 = 1 \times 3^3$, with the maximum exponent being $3$.
The fourth interval contains the number $36 = 1 \times 6^2$, with the maximum exponent being $2$.