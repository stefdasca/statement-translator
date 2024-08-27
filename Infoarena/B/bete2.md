## Task

Gigel received a large box full of $N$ sticks of different lengths as a gift. Being very inventive, he tries all kinds of games with the sticks. Now he aims to form distinct groups of three sticks such that the sum of the lengths of two sticks is equal to the length of the third one. Help Gigel determine the number of possibilities to form distinct groups of three sticks such that the length of one is equal to the sum of the lengths of the other two. 

## Input data

The input file `bete2.in` contains on the first line the natural number $N$, representing the number of sticks. The next $N$ lines each contain a natural number $x$, representing the lengths of the sticks. These numbers are distinct.

## Output data

The output file `bete2.out` will contain a single natural number, representing the number of possibilities to form distinct groups of three sticks such that the length of one is equal to the sum of the lengths of the other two.

## Constraints and clarifications

$1 \leq N \leq 3000$

$1 \leq x \leq 1\ 000\ 000\ 000$ 

Two groups of sticks are considered distinct if at least one length from one group is not found among the lengths of the other group.

## Example

`bete2.in`
```
10
17
4
13
12
5
29
6
11
18
7
12
```

`bete2.out`
```
12
```

## Explanation

$17 = 13 + 4$,  
$17 = 12 + 5$,  
$17 = 11 + 6$,  
$13 = 7 + 6$,  
$12 = 7 + 5$,  
$29 = 18 + 11$,  
$29 = 17 + 12$,  
$11 = 7 + 4$,  
$11 = 6 + 5$,  
$18 = 13 + 5$,  
$18 = 12 + 6$,  
$18 = 11 + 7$