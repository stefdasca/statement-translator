Gigel has to solve the following problem: consider the natural number $N$ composed of at most $9$ digits, all distinct and without the digit $0$. Gigel will have to make slips of paper for each digit in the number, slips that he will put into a hat, according to the following algorithm: initially, he starts from the last digit of the number (the units digit) and puts into the hat the slip of paper on which this digit is written. If this digit is even, he starts traversing the number to the right, otherwise to the left, traversing a number of steps equal to the respective digit. When traversing a number to the right, it is considered that after the last digit follows the first (the most significant digit of the number), followed by the second, etc., and when moving to the left after the first digit (the most significant digit of the number) follows the last digit (the units digit), then the second to last, etc., and the traversal starts with the digit immediately next to the digit written on the last slip of paper inserted into the hat, following the direction of traversal. For example, if our number is $1346$, Gigel starts with the digit $6$, and the slip of paper on which this digit is written is put into the hat. He traverses the number to the right, taking $6$ steps; passes through the digits: $1$, $3$, $4$, $6$, $1$ and stops at the digit $3$. Thus, in the hat will be put the slip of paper on which the digit $3$ is written.

The algorithm continues until all slips of paper are used up or when he reaches a digit for which the slip of paper with the respective value has already been put into the hat.

# Task

If the algorithm ends because Gigel has put all the slips of paper into the hat, the digit on the last slip of paper inserted into the hat will be printed, and if Gigel reaches during the traversal a digit for which the corresponding slip of paper has already been put into the hat, the value of this digit will be printed.

# Input data

The input file `numar.in` contains a single integer $N$.

# Output data

The output file `numar.out` will contain the digit at which Gigel stopped when the algorithm ended.

# Constraints and clarifications

* $1 \leq n < 10^9$;
* $n$ does not contain zero digits.

# Example 1

`numar.in`
```
412
```

`numar.out`
```
4
```

## Explanation

Gigel starts with the digit $2$ (the slip with the digit $2$ is put by Gigel into the hat); being an even value, he traverses to the right and stops at the digit $1$, the slip with this digit being put into the hat. The digit $1$ being odd, he continues the traversal to the left and stops at the digit $4$ and thus puts the last slip into the hat. From this moment there are no more slips to put into the hat and the digit $4$ will be printed.

# Example 2

`numar.in`
```
1243
```

`numar.out`
```
3
```

## Explanation

Gigel starts with the digit $3$ (the slip with the digit $3$ is put by Gigel into the hat); being an odd value, he traverses to the left and stops at the digit $1$, the slip with this digit being put into the hat. The digit $1$ being odd, he continues the traversal to the left and stops again at the digit $3$, but there is no slip with the digit $3$ left to be put into the hat. Therefore, the digit $3$ will be printed.