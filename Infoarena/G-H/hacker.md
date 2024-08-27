## Task

Nargy wants to find Fumeanu's email password to play a prank on him. After some investigation, Nargy discovered that Fumeanu's password is a number with $N$ digits in base $K$ that has the following property: any prefix of length $i < N$ of the number is different from the corresponding suffix of length $i$. Furthermore, Nargy knows which digits are at certain positions in the password. Not being a very skilled hacker, the only method Nargy knows to crack a password is brute force. Thus, he would like to know in advance how many possibilities exist for Fumeanu's password, using the information he has so far.

## Input data

The input file `hacker.in` contains on the first line the numbers $N$ and $K$. The next line contains $N$ characters, which can be numbers between $0$ and $K-1$ or the character `?` for the positions in the password that are unknown.

## Output data

The output file `hacker.out` will contain the number of possible passwords for Fumeanu, modulo $666013$.

## Constraints and clarifications

$1 \leq N \leq 200$

$2 \leq K \leq 10$

The number can start with digit $0$

## Example

`hacker.in`
```
4 2
1??0
```

`hacker.out`
```
3
```

## Explanation

The 3 possible passwords: `1000` `1100` `1110`

`1010` is not a valid password because the prefix of length $2$ (`10`) is equal to the suffix of length $2$ (`10`).