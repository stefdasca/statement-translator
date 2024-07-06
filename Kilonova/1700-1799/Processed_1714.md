## Task

Let $N$ be a natural number with the property that $(N, 10) = 1$.

Determine the period length $T$ of the simple periodic decimal fraction $\\frac{1}{N}$.

## Examples:

$N = 3$, $\\frac{1}{N} = 0.33333...$, so $T = 1$  
$N = 21$, $\\frac{1}{N} = 0.0476190476...$, so $T = 6$  
$N = 31$, $\\frac{1}{N} = 0.032258064516129032258064...$, so $T = 15$  
$N = 363$, $\\frac{1}{N} = 0.00275482093663911845730027548209...$, so $T = 22$

## Task

You need to write a program that reads the natural number $N$ and determines the number $T$ with the above meaning.

## Input data

The input file `perioada.in` contains on the first line the natural number $N$.

## Output data

The output file `perioada.out` will contain on the first line the number $T$ with the above meaning.

## Constraints and clarifications

* $2 < N < 10^{12}$
* $N$ and $10$ are coprime

## Example 1

`perioada.in`
```
3
```

`perioada.out`
```
1
```

### Explanation

The period of the fraction $\\frac{1}{3}$ is $1$.

## Example 2

`perioada.in`
```
21
```

`perioada.out`
```
6
```

### Explanation

The period of the fraction $\\frac{1}{21}$ is $6$.

## Example 3

`perioada.in`
```
31
```

`perioada.out`
```
15
```

### Explanation

The period of the fraction $\\frac{1}{31}$ is $15$.

## Example 4

`perioada.in`
```
363
```

`perioada.out`
```
22
```

### Explanation

The period of the fraction $\\frac{1}{363}$ is $22$.