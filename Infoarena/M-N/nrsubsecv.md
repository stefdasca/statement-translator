# Nrsubsecv

Sandu the Great Thinker is known for constantly asking himself many philosophical questions. Today, having an array of $N$ elements, he wants to answer $M$ questions of the form: Given $x$ and $y$, how many subarrays of the given array have the minimum element between $x$ and $y$? You need to show SMC that you are just as concerned with philosophical matters as he is, and answer his $M$ questions.

## Input data

The input file `nrsubsecv.in` contains on the first line two natural numbers $N$ and $M$, representing the number of elements in the array and the number of SMC's questions, respectively. The second line contains $N$ natural numbers, representing the elements of the array. The following $M$ lines each contain two natural numbers $x$ and $y$, $x \leq y$, as described in the prompt.

## Output data

The output file `nrsubsecv.out` must contain $M$ lines, each containing the answer to the $i$-th question from the input file.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$ 

$1 \leq M \leq 100\ 000$ 

Elements of the array are in the range $[0, 10^6]$ 

$0 \leq x \leq y \leq 10^6$ 

Attention! SMC recommends 64-bit signed data types to display the answer.

## Example

`nrsubsecv.in`

```
12 3
2 4 3 2 5 2 3 5 7 1 3 2
2 2
2 3
3 5
```

`nrsubsecv.out`

```
37
6
3
```

## Explanation

The $37$ subarrays that have a minimum of $2$ are: $[1, 1]$, $[1, 2]$, $[1, 3]$, $[1, 4]$, $[1, 5]$, $[1, 6]$, $[1, 7]$, $[1, 8]$, $[1, 9]$, $[2, 4]$, $[2, 5]$, $[2, 6]$, $[2, 7]$, $[2, 8]$, $[2, 9]$, $[3, 4]$, $[3, 5]$, $[3, 6]$, $[3, 7]$, $[3, 8]$, $[3, 9]$, $[4, 4]$, $[4, 5]$, $[4, 6]$, $[4, 7]$, $[4, 8]$, $[4, 9]$, $[5, 6]$, $[5, 7]$, $[5, 8]$, $[5, 9]$, $[6, 6]$, $[6, 7]$, $[6, 8]$, $[6, 9]$, $[11, 12]$ and $[12, 12]$.