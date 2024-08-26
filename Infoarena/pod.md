## Task

Little Red Riding Hood's path to her grandmother's house passes through the Enchanted Forest, a forest traversed by a river. Over this river, there is a single bridge made of $N$ planks. While crossing the bridge, Little Red Riding Hood can take steps of length 1 or $K$. Unfortunately, the bridge has $M$ missing planks (the positions of which are known to Little Red Riding Hood), on which she cannot step. Being an advocate of diversity, Little Red Riding Hood wants her stepping configuration to be different every day she visits her grandmother, so she asks you to figure out in how many ways she can reach the $N$-th plank. However, being aware that this number can be extremely large, she is content to know the result modulo 9901.

## Input data

The input file `pod.in` will contain on the first line 3 numbers, $N$, $M$ and $K$, having the significance described above. The second line will contain $M$ natural numbers, representing the positions of the missing planks.

## Output data

The output file `pod.out` will contain a single natural number, the remainder of the number of possibilities modulo 9901.

## Constraints and clarifications

$1 \leq N \leq 1 \, 000 \, 000 \, 000$

$0 \leq M \leq 1 \, 000$

$1 \leq K \leq 20$

For 15% of the tests $N \leq 1 \, 000 \, 000$

For another 15% of the tests $M = 0$

## Example

`pod.in`
```
10 3 2
1 4 6
```

`pod.out`
```
3
```