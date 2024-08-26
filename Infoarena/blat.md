# Blat

The Komisia has met to discuss the $M$ problems proposed for the FMICUSTRESS contest. Out of the $M$ proposed problems, they have to choose $N$ that will be given in the contest. It is also known that $K$ students have registered for the contest. Clearly, the Komisia wants to give the hardest problems to discourage the students, and for this, they have spent all the money received from sponsors for pizza on an analysis of the $K$ students. Thus, they received a matrix with $K$ rows and $M$ columns, where position $(i, j)$, i.e., the element at the $i$-th row and $j$-th column, represents the points the $i$-th student would score on the $j$-th problem if it were given in the contest (part of the set of $N$ chosen problems). For a set of problems, the score of student $i$ is the sum of the scores for each problem, that is, the sum of the elements from the $i$-th row and the columns corresponding to the chosen problems from the above matrix. The total score of a set of problems is the sum of the scores of each student. Since the Komisia cannot decide on which set of problems to choose, you are asked to determine: The highest and lowest total scores among all possible sets of problems. The highest and lowest scores of a student among all possible sets of problems. If you have any doubts about the task, look at the first example. Note: The Komisia does not really care about the highest score that can be achieved because they still want to give the hardest problems, but they ask for this information to avoid suspicion.

## Input data

The input file `blat.in` contains in the first line $M$, $N$ and $K$. It is followed by $K$ lines, each with $M$ columns, representing the matrix received from the student analysis.

## Output data

The output file `blat.out` will contain 4 lines. 
- The first line contains the total maximum score.
- The second line contains the total minimum score.
- The third line contains the highest score of a student.
- The fourth line contains the lowest score of a student.

## Constraints and clarifications

$1 \leq N$, $M$, $K \leq 100$  
$N \leq M$  
The elements of the matrix are natural numbers in the range $[0, 100]$.  
For tests worth 20 points (tests 1-2), each contestant will have the same score on all problems (although two different contestants may have different scores).  
For other tests worth 30 points (tests 3-4-5), 
$1 \leq N$, $M$, $K \leq 10$

## Example

`blat.in` 
```
5 3 4 
10 10 20 20 30 
20 10 20 30 10 
20 20 20 20 20 
30 30 30 30 30
```

`blat.out` 
```
280 
240 
90 
40 
```

## Explanation

If we choose the set of problems to be $\{1, 2, 3\}$, the total score would be $240$, because: 
- the first student will have $40$ points,
- the second student will have $50$ points,
- the third student will have $60$ points,
- the fourth student will have $90$ points.

To maximize the total score, we can choose the problems $3$, $4$, and $5$, with the total score being $280$. 
To minimize the total score, we can choose the problems $1$, $2$, and $3$, with the total score being $240$. 
The maximum score of a student is obtained when choosing problems $1$, $3$, and $5$, with the fourth contestant scoring $90$ points. 
The minimum score of a student is obtained when choosing problems $1$, $2$, and $4$, with the first contestant scoring $40$ points.