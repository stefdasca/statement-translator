## Task

Miruna thought it wasn't fair that only the juniors were tormented by a problem at yesterday's qualifier. So she decided to come back with another problem today. On a string $s$, she defines a border as a prefix of the string which is also a suffix and for which the two occurrences (at the beginning and end of the string) do not overlap. Furthermore, Miruna wonders which of these borders of the string $s$ have at least three disjoint occurrences (that do not overlap). Therefore, she asks you to display both their number and the length of the largest border with this property.

## Input data

In the input file `granite.in` the first line contains the string $s$.

## Output data

In the output file `granite.out`, the first line should contain two numbers, separated by a space, representing the number of borders with at least three disjoint occurrences and the length of the largest such border. If there is no such border, print “0 0”.

## Constraints

The string $s$ contains only lowercase letters of the English alphabet.

### Subtasks 
Index Score 

## Constraints

1 
10 points 
1 $\leq$ length of $s$ $\leq$ 100 

2 
25 points 
1 $\leq$ length of $s$ $\leq$ 5000 

3 
65 points 
1 $\leq$ length of $s$ $\leq$ 1\ 000\ 000 

## Example

`granite.in` 
```
catdfcatcat
```

`granite.out` 
```
1 3
```