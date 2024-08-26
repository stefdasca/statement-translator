## Trees3

Badea Ion recently bought a plot of land where he planted some trees. Tired but satisfied after a whole day of planting trees, Badea Ion sat on his porch to admire his work. Sitting there and looking at the trees, he noticed that his trees were very unaesthetic. For this, he thought of borrowing the magic wand used by Badea Gheorghe to enlarge or shrink things to beautify his trees. The trees were planted in a line and each tree has a height of $X_i$ meters. Badea Ion considers the trees to be aesthetic if and only if there are no two consecutive trees where the height difference is greater than $D$. Using the magic wand, he can decrease or increase the height of a tree by 1 meter with a single touch. Also, the first and last trees were planted by Badea Ion's grandchildren and he does not want them to be modified.

## Task

Being tired both physically and mentally, Badea Ion asks for help and wants to know the minimum number of touches required for the trees to meet the above condition.

## Input data

The first line of the file `copaci3.in` contains 2 numbers, $N$ and $D$, representing the number of trees and the maximum height difference between 2 trees for them to not be unaesthetic.
The next line contains the heights of the $N$ trees in order.

## Output data

In the file `copaci3.out` print a single number representing the minimum number of touches with the wand that Badea Ion needs to perform.

## Constraints and clarifications

$1 \leq N \leq 100$

$0 \leq D \leq 10^9$

$0 \leq X_i \leq 10^9$

If it is not possible to achieve an aesthetic configuration, print $-1$ 
Badea Ion recommends using 64-bit integers to calculate the result

## Example

`copaci3.in`
```
4 2 
1 5 1 4
```

`copaci3.out`
```
3
```

## Explanation

Tree 2 is reduced by 2 meters, and tree 3 is increased by 1 meter.