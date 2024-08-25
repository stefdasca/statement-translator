# Stiva2

In Acaerg mythology, Mivas was the god of fire, and Nivas was the god of ice. Because they were bored at the Annual Congress of the Gods, they started to play using the stack they found by chance in the hall. Mivas's power is to create fireballs, while Nivas's power is to create ice cubes. In each of the $N$ seconds they have at their disposal, exactly one of them uses their power and inserts their creation into the stack. When an ice cube is placed in the stack over a fireball (or vice versa), the two elements transform into steam and disappear. Because the stack is fragile, an element introduced into the stack at second $i$ must be removed by moment $i + K$ at the latest; otherwise, the stack will break. Mivas and Nivas wonder in how many ways they can introduce fireballs and ice cubes into the stack such that it does not break during the $N$ seconds, and it is empty at the end? They know the result can be quite large, so they will be satisfied with the remainder of its division by $9973$.

##  Input data

The input file `stiva2.in` will contain on the first line the number $N$ of seconds, and $K$, the maximum lifetime of an element in the stack.

##  Output data

The output file `stiva2.out` will contain on the first line the number of possible ways, modulo $9973$.

##  Constraints and clarifications

$1 \leq N \leq 1000$  
$1 \leq K \leq N$  

The only way to remove an element from the stack is to place an element of the opposite type over it.

##  Example

`stiva2.in`  
`4 2`  

`stiva2.out`  
`4`

##  Explanation

The ways to introduce fireballs/ice cubes into the stack are: $FGGF$, $GFFG$, $FGFG$, $GFGF$. Note: $FFGG$ is not a valid introduction of the balls. $G$ represents the introduction of an ice cube into the stack, while $F$ represents a similar operation for a fireball.