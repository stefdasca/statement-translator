##  Triplets

Zaharel has a farm with $N$ animals, conveniently numbered from 1 to $N$. Observing the activity of the animals, he noticed that certain animals are friends with each other. Curious by nature, Zaharel wondered how many triplets of animals exist such that any two animals in the triplet are friends.

##  Input data

The input file `triplets.in` will contain on the first line two natural numbers $N$ $M$ separated by a space, representing the number of animals and the number of friendship relations.

##  Output data

The output file `triplets.out` will contain a single natural number on the first line representing the number of triplets that can be formed.

##  Constraints and clarifications

$1 \leq N \leq 4096$ 

$1 \leq M \leq 65536$ 

If animal $a$ is friends with animal $b$, then animal $b$ is friends with animal $a$.

All friendship relations in the input file are distinct.

##  Example

`triplets.in` 

```
4 5
1 2
2 3
1 3
2 4
3 4
```

`triplets.out` 

```
2
```