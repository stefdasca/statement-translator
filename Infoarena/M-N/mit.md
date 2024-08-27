# Mit

Dumitiran, a professor at MIT (Multa Informatica pe Tava), has created an ingenious system for grading students at the end of the semester. He knows the grades of each student from the SD exam (these being on His List, indexed from $1$), but he wants to give a bonus to several of them according to the regulations from the beginning of the semester. However, he has forgotten which students deserved that bonus but has vague information. Dumitiran can apply $2$ types of operations:
$ \text{type 1:} $ he wants to know the highest grade of students in the interval $A - B;$
$ \text{type 2:} $ he knows there are some worthy students in the interval $A - B,$ but not knowing exactly which, decides to give a bonus of $X$ points to all students in this interval.

## Input data

The input file `mit.in` will contain on the first line $2$ numbers $N$ and $T,$ representing the number of students on Dumitiran's list and the number of operations he applied, respectively. The second line will contain $N$ numbers representing the initial grades of the students. The following $T$ lines will contain information about the operations: 
$1$ $A$ $B$ (if it is a type $1$ operation) or $2$ $A$ $B$ $X$ if it is a type $2$ operation. 

## Output data

The output file `mit.out` will contain the answers to type $1$ operations, one per line. 

## Constraints and clarifications

$1 \leq N, T \leq 100.000$

For $40$ points, 
$1 \leq N, T \leq 1.000$ 
(tests $1-4$)

For $20$ points, 
there will be at most $50$ type $2$ operations 
(these being the first in the input), 
and all others will be of type $1$ 
(at the end of the input), 
(tests $5-6$)

The initial grades are positive natural numbers $\leq 10.000$

$1 \leq X \leq 10.000$ for any of the tests 

## Example

`mit.in`
```
7 4
1 2 0 4 5 1 2
1 2 5
2 3 6 3
2 1 5 1
```

`mit.out`
```
4
5
8
```