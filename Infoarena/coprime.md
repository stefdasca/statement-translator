## Task

Miruna distributed several chocolate candies to her classmates. She no longer remembers exactly how many candies she gave to each colleague, but she knows for any two people whether the candies they received were coprime or not. Help the girl figure out how many candies she handed out to each colleague!

## Input data

The input file $coprime.in$ contains on the first line two natural numbers $N$ and $M$, representing the number of classmates and the number of pairs of colleagues that received coprime candies, respectively. The next $M$ lines will contain $2$ distinct natural numbers between $1$ and $N$, representing a pair.

## Output data

In the output file $coprime.out$ you will print $N$ lines, where on line $i$ there will be a natural number representing the number of candies received by the colleague with index $i$.

## Constraints and clarifications

$1 \leq N \leq 40$

$0 \leq M \leq N*(N-1)/2$

The values printed must be strictly greater than $0$ and can have at most $150$ digits.

You can print any solution that meets the imposed conditions.

## Example

$coprime.in$

```
2 1
1 2
```

$coprime.out$

```
2
3
```

$coprime.in$

```
2 0
```

$coprime.out$

```
4
4
```

$coprime.in$

```
4 4
1 2
1 3
1 4
2 3
```

$coprime.out$

```
15
14
21
22
```