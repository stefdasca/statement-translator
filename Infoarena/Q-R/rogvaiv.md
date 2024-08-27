# Rogvaiv

Consider $N$ dewdrops in a line. Each dewdrop can shine independently of how the others shine, due to the way the sun hits it, in the 7 colors of the rainbow: Red, Orange, Yellow, Green, Blue, Indigo, and Violet. Marcel is passionate about rainbows and therefore asks you, for ## task $C = 1$ , what is the number of ways in which the $N$ dewdrops can shine so that there are 7 consecutive drops that shine, in turn, from left to right, Red, Orange, Yellow, Green, Blue, Indigo, and Violet? For ## task $C = 2$ , Marcel wonders something deeper, namely how many ways the $N$ dewdrops can shine such that there are 7 consecutive dewdrops that shine ROGVAIV either from left to right or from right to left?

## Input data

The input file `rogvaiv.in` contains the numbers $C$ , $N$ , and $M$ .

## Output data

The output file `rogvaiv.out` contains the number of ways the $N$ dewdrops can shine so that Marcel sees at least one continuous ROGVAIV sequence. If $C = 1$ , he looks only from left to right, but if $C = 2$ , he looks both from right to left and left to right. The answer is required modulo $M$ .

## Constraints and clarifications

The 3 numbers in the input are integers.
$$1 \leq C \leq 2$$
$$1 \leq N \leq 50000$$
$$2 \leq M \leq 10^9 + 10$$

**Scoring:**
Evaluation will be done on 10 tests, each worth 10 points.
The tests are not grouped.
Tests 1, ..., 5 have $C = 1$ and tests 6, ..., 10 have $C = 2$.
Tests 1, 2, 6, and 7 have $M = 10^9 + 7$.
Tests 3, 4, 8, and 9 have $M$ as a prime number.

## Example

`rogvaiv.in`
```
1 7 10
1
2 7 10
2
2 7 2
0
1 50000 10000
4984
2 50000 1000000007
216329628
```

## Explanation

For the first example, the only way the dewdrops can shine is "ROGVAIV". For the second example, there are two ways the dewdrops can shine: "ROGVAIV" and "VIAVGOR". For the third example, the output is $2 \mod 2 = 0$. Note that the two $V$’s actually represent distinct colors, Green and Violet.