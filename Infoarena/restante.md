## Task

Wef and Astro have many outstanding tasks at college and have decided to go to a place to consume natural orange juice. When they received the bill, they noticed that the bill contains $N$ words made up of lowercase letters of the Latin alphabet. Wef says that some words are not original and challenges Astro to find the number of original words. A word $A$ is original if there is no other word $B$ written on the bill such that if we permute the letters in a certain order, we obtain the word $A$. For example, if the list contains the words $abc$, $cba$, and $bbb$, the only original word is $bbb$. The other two words can be obtained from each other by changing the order of the letters.

## Input data

The input file `restante.in` contains on the first line the number $N$ as mentioned in the task. Then follow the $N$ words on the bill, each word having a maximum of $16$ characters.

## Output data

The output file `restante.out` contains on the first line the number $NR$, representing the number of original words on the bill.

## Constraints and clarifications

$1 \leq N \leq 36000$  
Each word has a maximum of $16$ characters

## Example

`restante.in`  
```
3
abc
cba
bbb
```

`restante.out`  
```
1
```