## Disaster

The Day of Disaster has arrived. According to L. Ron Hubbard, due to the low number of people enrolled in Scientology, extraterrestrials will subject Earth to $N$ consecutive attacks. Besides the fact that they have built a shield that will protect Earth after the first $K$ assaults, people have calculated the probabilities $p_1$, $p_2$, $\dots$ $p_N$ of surviving each of the planned attacks. Only one problem remains: the order in which these attacks will occur is unknown, with each of the $N!$ permutations being equally probable. You know that the probability of surviving $x$ attacks is equal to the product of the individual probabilities. You are asked to calculate the probability that Earth will withstand the first $K$ attacks, thereby saving itself from Disaster.

## Input data

The first line of the file `dezastru.in` contains the natural and positive numbers $N$ and $K$. The next line contains $N$ real numbers, representing the probability that Earth withstands each of the expected $N$ attacks.

## Output data

The first line of the file `dezastru.out` will contain a single real number with 6 decimal places: the probability of surviving the first $K$ attacks, after which Earth will activate the cosmic shield. The answer will be checked with a precision of $0.000001$.

## Constraints and clarifications

$1 \leq N \leq 25$

$K \leq N$

## Example

`dezastru.in`
```
3 2
0.3 0.5 0.8
```

`dezastru.out`
```
0.263333
```

## Explanation

Permutation Probability of surviving the first 2 attacks:

1 2 3 $\rightarrow 0.3 \times 0.5 = 0.15$

1 3 2 $\rightarrow 0.3 \times 0.8 = 0.24$

2 1 3 $\rightarrow 0.5 \times 0.3 = 0.15$

2 3 1 $\rightarrow 0.5 \times 0.8 = 0.40$

3 1 2 $\rightarrow 0.8 \times 0.3 = 0.24$

3 2 1 $\rightarrow 0.8 \times 0.5 = 0.40$

There are a total of 6 permutations so each will occur with a probability of $\frac{1}{6}$.

Solution: $\frac{0.15}{6} + \frac{0.24}{6} + \frac{0.15}{6} + \frac{0.40}{6} + \frac{0.24}{6} + \frac{0.40}{6} = 0.263333$