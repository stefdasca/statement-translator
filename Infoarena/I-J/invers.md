## Task 

Help Zaharel study the aforementioned property of numbers on paper by creating a program.

## Input Data 

The file `invers.in` will contain on the first line a natural number $T$, which represents how many numbers are written on the paper. The next $T$ lines will contain the natural numbers written on the paper, one per line.

## Output Data 

The file `invers.out` will contain $T$ lines, each containing the text "DA" (if the corresponding number from the input file can be written as $x+Inv(x)$) or "NU" (otherwise).

## Constraints and clarifications

$1 \leq T \leq 10\ 000$

$0 < Nr < 10^{10\ 000}$

## Example 

`invers.in` 

```
6
13
11
4774
2
1
120219482301
```

`invers.out`

```
NU
DA
DA
DA
NU
DA
```

## Explanations 

$10 + Inv(10) = 11$ 

$4700 + Inv(4700) = 4774$ 

$1 + Inv(1) = 2$ 

$23918700369 + Inv(23918700369) = 120219482301$