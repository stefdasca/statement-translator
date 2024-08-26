# Easy Choice

This year, Colonel James has been tasked with recruiting soldiers for his country's army. During the recruitment, $N$ candidates appear, each being characterized by their height (a natural number). Colonel James wants to form $R$ divisions, each with $C$ soldiers, and the rest of the candidates should be rejected. Within a division, we define the "imbalance" as the maximum difference in heights between any 2 soldiers. The "imbalance" of the entire army is the maximum of the imbalances of the $R$ divisions. For performance reasons, the colonel wishes to recruit soldiers such that the army has the minimum imbalance. Help him achieve his task!

## Input data

The input file `easychoice.in` contains on the first line the numbers $N$, $R$, and $C$ separated by a space, having the meanings described above. The second line contains $N$ numbers representing the candidates' heights.

## Output data

The output file `easychoice.out` will contain a single natural number representing the minimum imbalance obtained in recruiting the soldiers.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$1 \leq R \times C \leq N$

The height $H$ of a candidate adheres to the restriction $1 \leq H \leq 1\ 000\ 000\ 000$

Something needs to be done against high-calorie meals.

For 50% of the tests, $N \leq 1\ 000$

## Example

`easychoice.in`

```
8 2 3
183 218 238 203 273 143 238 173
```

`easychoice.out`

```
30
```

## Explanation

The following soldiers can be chosen:

Division 1: $238, 218, 238$ (imbalance $20$)

Division 2: $173, 203, 183$ (imbalance $30$)

The imbalance of the army is $\max(20, 30) = 30$ .