# Senate

In the Parliament of a democratic country, each senator can be a member of zero or more parliamentary committees. Each committee has a president, elected from among its members. Based on democratic principles, a senator can be president of at most one committee. Now the senate wants to determine a way to choose the presidents for each committee so that no two committees have the same president.

## Task

Determine a possible assignment of presidents for each committee.

## Input data

In the input file $senat.in$, the first line contains the number $N$ of senators, and the second line contains the number $M$ of committees. Each of the following $M$ lines describes the composition of a committee. A committee is defined by its members, separated by a space.

## Output data

The output file $senat.out$ will contain exactly $M$ lines, with the $i$-th line containing the elected president for the $i$-th committee. If there is no solution, the output file will contain a single line with the number $0$.

## Constraints and clarifications

$1 \leq N \leq 100$

$1 \leq M \leq 100$

If there are multiple solutions, any of them can be displayed.

## Examples

$senat.in$ 
```
5 
3 
1 2 4 5 
3 1 3 4 
1 5
```
$senat.out$ 
```
3 
2 
1
```
$senat.in$ 
```
3 
2 
1 2 
1 2 
```
$senat.out$ 
```
1 
2
```
$senat.in$ 
```
2 
1 
2 
1 
```
$senat.out$ 
```
0
```