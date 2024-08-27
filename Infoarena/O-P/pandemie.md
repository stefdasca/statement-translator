# Pandemic

Humanity is facing a severe global pandemic due to the mielenevirus. Because of this, the International Enthusiastic Organization of Hospitals (IEOH) has decided to establish a medical center in the most advanced state, iGorj. The $N$ states (numbered from $1$ to $N$ with iGorj being state number $1$) around the world can be represented along with the bidirectional connections between them in the form of a tree. The mielenevirus is very unpredictable: people in state $X$ can heal instantly or all get sick spontaneously. Vladuri needs to solve $Q$ operations of the form:
$1$ $X$ - The $X$th state is infected
$2$ $X$ - The $X$th state is healed
$3$ $X$ - If he were in the $X$th state, which would be the closest state to iGorj that he could reach without passing through any infected state?
Help Vladuri determine the state for each type $3$ query.

## Input data

The input file `pandemie.in` will contain:
The first line contains a number $N$ with the meaning from the statement.
The following $N-1$ lines contain two numbers $A$ and $B$, representing a bidirectional road between the $A$th state and the $B$th state.
The next line contains a number $Q$ representing the number of queries.
The following $Q$ lines will contain two numbers $Op$ and $S$, $Op$ representing the type of operation, and $S$ representing the state on which the operation is applied.

## Output data

The output file `pandemie.out` will contain on each distinct line, a number representing the answer for each type $3$ query.

## Constraints and clarifications

$1 \leq N, Q \leq 120\ 000$
$1 \leq N, Q \leq 3000$ (For $40$ points)
$1 \leq N, Q \leq 50\ 000$ (For another $40$ points)

It is guaranteed that we will never start from an infected state.

It is guaranteed that the read bidirectional edges form a tree rooted at $1$.

## Example

`pandemie.in`
```
7 
1 2 
1 3 
2 4 
2 6 
2 7 
4 5 
3
1 1 
3 3 
1 2
3 6
2 1 
```

`pandemie.out`
```
1 
1 
6 
```

~[example.png]