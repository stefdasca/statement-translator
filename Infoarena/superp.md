# SuperP

As you might know, Ileana Cosânzeana has been passionate about prime numbers since she was a child. Since she learned what a prime number is, she kept playing with them and particularly enjoyed making problems involving prime numbers, which she then presented to everyone in her great kingdom. Ileana also invented SUPERPRIME numbers. She considers a number to be SUPERPRIME if it and any of its prefixes are prime numbers (e.g., $373$ is superprime because $3$ is prime, $37$ is prime, and $373$ is prime, whereas $43$ is not superprime because $4$ is not prime). Ileana grew up and the time came for her to find her chosen one. Many princes from all corners of the world came to woo the beautiful Ileana but failed to decipher her codes. On the day of $29-7-2333$, Fat Frumos came to the kingdom's gate. On the door, there were $N \leq 100$ numbers, each less than $10^{12}$, representing Ileana's famous codes. To enter the kingdom, Fat Frumos must, for each code, find the largest SUPERPRIME that can be formed with its digits. Help Fat Frumos enter the kingdom.

## Task

For each of the $N$ codes, find the largest SUPERPRIME number that can be formed with its digits.

## Input data

In the file `superp.in`, the first line contains a positive integer $N$, representing the number of codes on Ileana's door, and each of the following $N$ lines contains a code.

## Output data

The output file `superp.out` contains $N$ lines, the line $i$ containing a SUPERPRIME number representing the answer for the $i$-th code of Ileana.

## Constraints

$0 < N \leq 100$

For each code, there will be a SUPERPRIME number that can be formed with its digits.

Ileana's codes are integers in the interval $[1,10^{12}]$

For $50\%$ of the tests, Ileana's codes are less than $10^8$

The digits of a code can be used in any order to form a SUPERPRIME number, and it is not mandatory for the SUPERPRIME number to use all digits of the respective code.

## Example

`superp.in`

```
4
321
13
357
22
```

`superp.out`

```
31
31
73
2
```

## Explanation

$321$ is not superprime because $321$ is divisible by $3$, as well as any number formed with all $3$ digits. Two superprimes that can be formed using two digits are $31$ and $23$, thus $31$ will be the answer because it is the largest.