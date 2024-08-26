## Task 

We will call an $ (N,K) $ permutation a sequence of $ N \cdot K $ where each number between $ 1 $ and $ N $ appears exactly $ K $ times, and adjacent elements are different. Let $ S $ be the sequence of all $ (N,K) $ permutations ordered lexicographically. Write a program to implement the following operations:
A. Given a valid $ (N,K) $ permutation, determine its position in the sequence $ S $.
B. Given a natural number $ X $, determine the $ X $-th permutation in the sequence $ S $. 

## Input data 

The input file `nkperm.in` contains on the first line the natural numbers $ N $ $ K $ $ T $. The following $ T $ lines describe the operations, each line starting with a character ( $ A $ or $ B $ ) specifying the type of operation.
- If it's an operation of type $ A $, it will be followed by $ N \cdot K $ numbers that represent a valid $ (N,K) $ permutation.
- If it's an operation of type $ B $, it will be followed by a natural number $ X $.

## Output data 

The output file `nkperm.out` will contain $ T $ lines, each representing the result of the operations from the input file, in the order they were given:
- If it's an operation of type $ A $, a natural number $ X $ will be printed.
- If it's an operation of type $ B $, $ N \cdot K $ numbers will be printed, representing the $ X $-th valid $ (N,K) $ permutation.

## Constraints and clarifications

$ 1 \leq N \leq 20 $

$ 1 \leq K \leq 5 $

$ 1 \leq T \leq 1\ 000 $

It is guaranteed that for operation $ A $, the given permutation will have the position number less than $ 2^{55} $.

It is guaranteed that for operation $ B $, the given number $ X $ will be less than $ 2^{55} $.

## Example 

`nkperm.in` 
```
3 2 2 
A 1 3 2 1 2 3 
B 11 
```

`nkperm.out` 
```
7 
2 1 2 3 1 3 
```

## Explanation 

$ 1\ 2\ 1\ 3\ 2\ 3 $
$ 1\ 2\ 3\ 1\ 2\ 3 $
$ 1\ 2\ 3\ 1\ 3\ 2 $
$ 1\ 2\ 3\ 2\ 1\ 3 $
$ 1\ 2\ 3\ 2\ 3\ 1 $
$ 1\ 3\ 1\ 2\ 3\ 2 $
$ 1\ 3\ 2\ 1\ 2\ 3 $
$ 1\ 3\ 2\ 1\ 3\ 2 $
$ ...