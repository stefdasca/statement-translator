# Code

An array of $N$ lowercase letters of the English alphabet is given. By encoding, the array will be replaced by a sequence of its subarrays, each subarray being preceded by a number indicating how many times this subarray is repeated one after another in the array. We need to find an encoding of the given array so that the array obtained after encoding has the minimum length in terms of the number of characters. When determining the length of the encoding, the digits that form the numbers in front of the subarrays will also be considered.

## Task

We need to find an encoding of the given array so that the array obtained after encoding has the minimum length in terms of the number of characters.

## Input data

The first line of the file `cod.in` contains the number $N$. The next line contains $N$ characters forming the given array.

## Output data

The first line of the file `cod.out` contains an integer $L$, the minimum length of the encoded array. The next line contains $L$ characters that form a valid encoding of the initial array. If there are multiple possible valid minimum encodings, print any one of them.

## Constraints and clarifications

$1 \leq N \leq 2000$

Determining the correct minimum length provides 40% of the score.

40% of the tests will have $1 \leq N \leq 200$

## Example

`cod.in`
```
10 
aabacacacc
```

`cod.out`
```
9
2a1b3ac1c
```

## Explanation

Another possible solution is `1aab3ac1c`.