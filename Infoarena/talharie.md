## Task

Since there are so many concerts this summer, Miruna needs money to buy tickets. What better idea could the girl have than robbing a bank? Said and done, here she is in front of the safe. After threatening the bank manager with a gun to his temple, Miruna managed to get the special code of the safe. This is a sequence with $N$ characters that are lowercase letters of the alphabet. However, things are not as simple as they seem because to enter the room with money, the code must be deciphered. Miruna knows that she must rotate the string of characters exactly $K$ positions to the left and then repeat the same procedure until she reaches the initial string again. For a sequence of $N$ characters and a number $K$, find the lexicographically smallest string that can be obtained from the initial string by repeatedly rotating it circularly to the left by $K$ positions each time.

## Input data

The input file `talharie.in` contains the first line which contains a natural number $T$, representing the number of tests. The following $T$ lines contain two natural numbers $N$ and $K$, having the aforementioned significance, followed by a string of $N$ lowercase letters of the alphabet.

## Output data

The output file `talharie.out` will contain $T$ lines, on each line containing a string representing the lexicographically smallest string that can be obtained for each test.

## Constraints

$1 \leq T \leq 10$

$1 \leq N \leq 100000$

$0 \leq K \leq N$

A string $(x_1 ,x_2 \dots x_N)$ is lexicographically smaller than another string $(y_1 ,y_2 \dots y_M)$ if there exists a position $p$ such that $x_p < y_p$ and $x_1 = y_1$, $x_2 = y_2 \dots x_{p-1}= y_{p-1}$.

## Example

`talharie.in`
```
2 
4 0 abcd 
4 2 bbaa 
```

`talharie.out`
```
abcd 
aabb 
```

## Explanation

For the first test, the only possible string that can be obtained is $abcd$. For the second test, we can obtain $bbaa$ or $aabb$.