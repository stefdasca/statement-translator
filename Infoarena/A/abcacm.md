ABCacm

Gigel likes to play with numbers. He chose three natural numbers $A$, $B$, and $C$ and uses them to calculate a nice sequence of numbers. The nice sequence starts with two $0$s. The rest of the elements in the sequence are calculated using a simple rule based on the numbers $A$, $B$, and $C$. The $i$-th element $(i \geq 3)$ of the sequence is calculated as follows:
- multiply the $(i-2)$-th element by $A$
- multiply the $(i-1)$-th element by $B$
- add the results above together, and then add $C$

Gigel quickly got bored of writing the sequence, so he asks for your help. He gives you a natural number $i$ and asks you to calculate the $i$-th element of the sequence, modulo $9907$.

## Input data

The first line of the input file `abcacm.in` contains the number $T$ of tests. The following $T$ lines each contain 4 natural numbers $A$, $B$, $C$, and $i$, separated by spaces, as described above.

## Output data

The output file `abcacm.out` must contain $T$ lines, each containing the $i$-th element of the sequence, modulo $9907$, for the corresponding test.

## Constraints and clarifications

$1 \leq A \leq 2013$

$1 \leq B \leq 2014$

$1 \leq C \leq 2015$

$1 \leq i \leq 2^{31} - 1$

## Example

`abcacm.in`

```
1
1 2 3 4
```

`abcacm.out`

```
9
```

## Explanation

The sequence is $0$, $0$, $3$, $9$, $24$, $60$, $\dots$. The 4th element is $9$, and $9$ modulo $9907$ is $9$ (which should be printed).