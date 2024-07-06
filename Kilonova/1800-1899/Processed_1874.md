Andrei wants to create more statistics about his home library. He has taken the number of pages of each book and put it into an array. The first thing he wants to see is if all his books have an even number of pages. He managed to implement a C++ program, but it seems to return incorrect results.

## Task

He asks you to help him solve the problem. You can find the source written by Andrei [here](decisional.cpp) or in the "Attachments" section on the side.

## Input data

Read from the console. The first line contains a natural number $n$, and then the next line contains a sequence of $n$ integers representing the pages of each book read.

## Output data

Print to the console the message `Numarul de pagini al tuturor cartilor este par.` if the sequence read contains only books with an even number of pages. Otherwise, print the message `Unele carti au numar de pagini impar.`.

## Constraints and clarifications

- $3 < n < 2\ 000$
- The values in the array are natural and less than $1\ 000$.

## Example
`stdin`
```
5
629 103 413 401 9
```
`stdout`
```
Unele carti au numar de pagini impar.
```

