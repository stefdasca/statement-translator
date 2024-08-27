## Task

You are given a number $X$. You have seen many numbers in your life, you didn't really need another one. But since you've been given one, you try not to get bored. So you wonder: If you generate all distinct numbers that can be obtained by permuting the digits of $X$ and then sort them in ascending order, what is the maximum difference between two consecutive numbers in this sequence? If this doesn't work out, maybe you can present the number on "iUmor". Hopefully, it works out though.

## Input data

The input file `gap.in` will contain on its first line the number $T$, representing the number of tests. Each test will consist of a number $X$.

## Output data

The output file `gap.out` will contain $T$ lines, each containing the answer for the corresponding test.

## Constraints and clarifications

$1 \leq T \leq 10^5$ 

$1 \leq X \leq 10^{15}$ 

$X$ never contains the digit 0.

If there are no two distinct numbers in the generated sequence, the answer is considered to be 0.

## Example

`gap.in`
``` 
3 
1223 
55 
91 
```

`gap.out`
``` 
801 
0 
72 
```