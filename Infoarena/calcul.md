# Calculation

Bronzărel has grown up and will soon go to college. However, college admission is not that simple, with difficult tests such as mathematics. To prepare, Bronzărel works on mathematics daily, performing various calculations. Zăhărel wants to show Bronzărel that he can solve any math problem with the help of a computer and his programming skills. He asked Bronzărel to give him the hardest problem he knows! Bronzărel immediately wrote down the following sum on a piece of paper: $A_1 + A_2 + A_3 + \dots + A_B$ and told him that he only needs to calculate its value. Since the result can be a very large number, Bronzărel will be satisfied if Zăhărel determines only the last $C$ digits of the sum.

## Task

Imagine you are in Zăhărel's place and write a program to show Bronzărel that difficult math problems can be solved with the help of a computer!

## Input data

The first line of the file `calcul.in` will contain the natural number $A$, in base 10. The second line will contain the natural number $B$, which will be given in base 16, and the third line will contain the natural number $C$.

## Output data

The first line of the file `calcul.out` will contain the last $C$ digits of the sum mentioned above.

## Constraints

$0 \leq A \leq 10^{100\ 000}$

$1 \leq B \leq 16^{50\ 000}$

$1 \leq C \leq 9$

The digits in base 16 are $0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F$ (only uppercase)

For $20\%$ of tests $A \leq 10^9$ and $B \leq 16^4$

For $60\%$ of tests $B \leq 16^{1\ 000}$

For $50\%$ of tests $\text{gcd}(A-1, 10^C)=1$

## Examples

`calcul.in`

```
2
7
2
```

`calcul.out`

```
54
```

`calcul.in`

```
47
C
6
```

`calcul.out`

```
851680
```

`calcul.in`

```
23
1
9
```

`calcul.out`

```
000000023
```

## Explanations

$2_1 + 2_2 + 2_3 + 2_4 + 2_5 + 2_6 + 2_7 = 2_{54}$

$47_1 + 47_2 + 47_3 + 47_4 + 47_5 + 47_6 + 47_7 + 47_8 + 47_9 + 47_{10} + 47_{11} + 47_{12} = 118\ 717\ 384\ 915\ 664\ 851\ 680$