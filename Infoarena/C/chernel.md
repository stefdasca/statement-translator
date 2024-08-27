## Task

Chernel has given up business and started studying mathematics. This time, he is studying special arrays. Chernel starts with an array of $N$ natural numbers $a_1, a_2, \dots, a_N$, upon which he applies successive transformations that change an array of $X$ elements $a_1, a_2, \dots, a_X$ into an array of $X-1$ elements $a_1 + a_2, a_2 + a_3, \dots, a_{X-1} + a_X$. Chernel repeats this operation until he is left with a single element. From this, he obtains the characteristic number of the array, which is the remainder when dividing that last remaining element by a natural number $M$. Chernel notices that the values of some elements in the initial array do not affect the characteristic number of the array, in other words, regardless of their value, the characteristic number remains the same. For given $N$ and $M$, help Chernel find out how many such values exist in the initial array.

## Input data

The input file `chernel.in` contains on the first line the two natural numbers $N$ and $M$.

## Output data

The output file `chernel.out` will contain on the first line a single natural number representing the number of elements in the initial array whose value does not affect the characteristic number of the array.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 1\ 000\ 000\ 000$

## Example

`chernel.in`

```
3 2
```

`chernel.out`

```
1
```

## Explanation

Let the initial array be $a_1, a_2, a_3$. It transforms into $a_1 + a_2, a_2 + a_3$ and then into $a_1 + 2*a_2 + a_3$. For $M = 2$, the only value in the initial array that does not affect the characteristic number is $a_2$.